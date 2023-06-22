import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InputFile
from tortoise.expressions import Q

from bot.core.constants import is_num_regex
from bot.db.models import Expense, User, Income, Category, Operation
from bot.db import utils
from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard, f_cb
from bot.handlers.keyboards.categories_keyboard import categories_keyboard, cb
from bot.handlers.keyboards.graph_keyboard import graph_keyboard
from bot.handlers.states.add_expense import AddExpenseState
from bot.handlers.states.add_income import AddIncomeState
from bot.misc import dp, bot
from bot.services import graphs


@dp.callback_query_handler(text='finances_menu', state='*')
async def finances_menu(call: CallbackQuery):
    await call.answer()
    user = await User.filter(telegram_id=int(call.message.chat.id)).first()
    operations = await Operation.filter(user=user).order_by('-date').limit(5).all()
    operations = [await Expense.filter(id=operation.operation_id).first() if operation.operation_type == 'expense'
                  else await Income.filter(id=operation.operation_id).first()
                  for operation in operations]
    operations = '\n'.join([f'{i + 1} +{operations[i].sum / 100} {operations[i].date.strftime("%d-%m-%Y")}'
                  if isinstance(operations[i], Income) else
                  f'{i + 1} -{operations[i].sum / 100} {(await operations[i].category).name} {operations[i].date.strftime("%d-%m-%Y")}'
                  for i in range(len(operations))])
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
    await call.answer()
    callback_data['page'] = int(callback_data['page'])
    if callback_data['page'] < 1:
        return
    user = await User.filter(telegram_id=int(call.message.chat.id)).first()
    operations = await Operation.filter(user=user).order_by('-date').offset\
        (5 * (callback_data['page'] - 1)).limit(5 * callback_data['page']).all()
    operations = [await Expense.filter(id=operation.operation_id).first() if operation.operation_type == 'expense'
                  else await Income.filter(id=operation.operation_id).first()
                  for operation in operations]
    for o in operations:
        print(type(o))
    operations = '\n'.join([f'{5 * (callback_data["page"] - 1) + i + 1} +{operations[i].sum / 100} {operations[i].date.strftime("%d-%m-%Y")}'
                            if isinstance(operations[i], Income) else
                            f'{5 * (callback_data["page"] - 1) + i + 1} -{operations[i].sum / 100} {(await operations[i].category).name} {operations[i].date.strftime("%d-%m-%Y")}'
                            for i in range(len(operations))])
    if not operations:
        return
    msg = f'''
Ваши операции:
{operations}
'''
    await call.message.edit_text(msg)
    keyboard = await finances_menu_keyboard(callback_data['page'])

    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text='add_expense')
async def add_expense(call: CallbackQuery):
    await call.answer()
    keyboard = await categories_keyboard([(category.id, category.name) for category in (await Category.all())])
    await AddExpenseState.category.set()
    await call.message.answer('Выберите категорию', reply_markup=keyboard)


@dp.callback_query_handler(cb.filter(), state=AddExpenseState.category)
async def category_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(category=callback_data['el_id'])
    await AddExpenseState.next()
    await call.message.answer('Введите сумму')


@dp.message_handler(state=AddExpenseState.sum, regexp=is_num_regex)
async def expense_sum_entered(message: Message, state: FSMContext):
    await state.update_data(sum=float(message.text) * 100)
    data = await state.get_data()
    await save_expense(data, message, state)


async def save_expense(data, message, state):
    data['category'] = await Category.filter(id=int(data['category'])).first()
    data['date'] = datetime.datetime.now()
    data['user'] = await User.filter(telegram_id=message.from_user.id).first()
    expense = Expense(**data)
    await expense.save()
    await Operation(operation_type='expense',
                    operation_id=expense.id,
                    date=data['date'],
                    user=data['user']).save()
    await message.answer("Список Ваших расходов пополнен")
    await state.finish()


@dp.callback_query_handler(text='add_income')
async def add_income(call: CallbackQuery):
    await call.answer()
    await AddIncomeState.sum.set()
    await call.message.answer('Введите сумму')


@dp.message_handler(state=AddIncomeState, regexp=is_num_regex)
async def income_sum_entered(message: Message, state: FSMContext):
    await state.update_data(sum=float(message.text) * 100)
    data = await state.get_data()
    await save_income(data, message, state)


async def save_income(data, message, state):
    data['date'] = datetime.datetime.now()
    data['user'] = await User.filter(telegram_id=message.from_user.id).first()
    income = Income(**data)
    await income.save()
    await Operation(operation_type='income',
                    operation_id=income.id,
                    date=data['date'],
                    user=data['user']).save()
    await message.answer("Список Ваших доходов пополнен")
    await state.finish()


@dp.callback_query_handler(text='export_data')
async def export_data(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Выберите график', reply_markup=await graph_keyboard())


@dp.callback_query_handler(text='year_graph_line')
async def year_graph(call: CallbackQuery):
    await call.answer()
    year = datetime.datetime.now().year
    user = await User.filter(telegram_id=call.message.chat.id).first()
    path = graphs.year_graph_line(*(await utils.data_months(year, user)))
    await bot.send_photo(user.telegram_id, InputFile(path))


@dp.callback_query_handler(text='cat_month_graph')
async def cat_month_graph(call: CallbackQuery):
    month = datetime.datetime.now().month
    user = await User.filter(telegram_id=call.message.chat.id).first()
    data = await utils.data_days_categories(month, user)
    path = graphs.mounth_graph_bars(data.keys(), data.values())
    await bot.send_photo(user.telegram_id, InputFile(path))


@dp.callback_query_handler(text='year_graph_bar')
async def year_graph(call: CallbackQuery):
    await call.answer()
    year = datetime.datetime.now().year
    user = await User.filter(telegram_id=call.message.chat.id).first()
    path = graphs.year_graph_bars(*(await utils.data_months(year, user)))
    await bot.send_photo(user.telegram_id, InputFile(path))

