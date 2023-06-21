import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.constants import is_num_regex
from bot.db.models import Expense, User, Income, Category
from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard, f_cb
from bot.handlers.keyboards.categories_keyboard import categories_keyboard, cb
from bot.handlers.states.add_income import AddIncomeState
from bot.misc import dp


@dp.callback_query_handler(text='finances_menu', state='*')
async def finances_menu(call: CallbackQuery):
    await call.message.delete()
    user = await User.filter(telegram_id=int(call.message.chat.id)).first()
    expenses = await user.expenses.all()
    incomes = await user.incomes.limit(5).all()
    operations = list(sorted(expenses + incomes, key=lambda x: x.date))
    operations = '\n'.join([f'{op.id} {op.sum} {op.date}'
                  if isinstance(op, Income) else
                  f'{op.id} {op.sum} {(await op.category).name} {op.date}'
                  for op in operations])
    msg = f'''
Ваши операции:
{operations}
'''
    await call.message.answer(msg, reply_markup=
    (await finances_menu_keyboard(1)))


@dp.callback_query_handler(f_cb.filter())
async def change_page(call: CallbackQuery, callback_data: dict):
    print('hi')
    print(callback_data['page'])
    callback_data['page'] = int(callback_data['page'])
    if callback_data['page'] < 1:
        return
    user = await User.filter(telegram_id=int(call.message.chat.id)).first()
    expenses = await user.expenses.offset(5 * (callback_data['page'] - 1)).limit(5 * callback_data['page']).all()
    incomes = await user.incomes.offset(5 * (callback_data['page'] - 1)).limit(5 * callback_data['page']).all()
    operations = list(sorted(expenses + incomes, key=lambda x: x.date))
    print(operations)
    operations = '\n'.join([f'{op.id} {op.sum} {op.date}'
                            if isinstance(op, Income) else
                            f'{op.id} {op.sum} {(await op.category).name} {op.date}'
                            for op in operations])
    msg = f'''
Ваши операции:
{operations}
'''
    await call.message.edit_text(msg)
    keyboard = await finances_menu_keyboard(callback_data['page'] + 1)


@dp.callback_query_handler(text='add_expense')
async def add_income(call: CallbackQuery):
    keyboard = await categories_keyboard([(category.id, category.name) for category in (await Category.all())])
    await AddIncomeState.category.set()
    await call.message.answer('Выберите категорию', reply_markup=keyboard)


@dp.callback_query_handler(cb.filter(), state=AddIncomeState.category)
async def category_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(category=callback_data['el_id'])
    await AddIncomeState.next()
    await call.message.answer('Введите сумму')


@dp.message_handler(state=AddIncomeState.sum, regexp=is_num_regex)
async def sum_entered(message: Message, state: FSMContext):
    await state.update_data(sum=float(message.text) * 100)
    data = await state.get_data()
    await save_income(data, message, state)


async def save_income(data, message, state):
    data['category'] = await Category.filter(id=int(data['category'])).first()
    data['date'] = datetime.datetime.today()
    data['user'] = await User.filter(telegram_id=message.from_user.id).first()
    await Expense(**data).save()
    await message.answer("Список Ваших расходов пополнен")
    await state.finish()
