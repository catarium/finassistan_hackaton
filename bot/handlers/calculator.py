from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.config import config
from bot.core.constants import is_num_regex, is_int_regex
from bot.db.models import Expense, User, Income, Category, Advice
from bot.handlers.keyboards.calculator_menu_keyboard import calculator_menu_keyboard
from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard
from bot.handlers.states.admin import AdminState
from bot.handlers.states.breakeven_poin import BreakEvenPointState
from bot.handlers.states.create_advice import AdviceState
from bot.handlers.states.create_category import CreateCategoryState
from bot.handlers.states.delete_advice import DeleteAdviceState
from bot.handlers.states.delete_cateogory import DeleteCategoryState
from bot.misc import dp


@dp.callback_query_handler(text='calculator_menu')
async def calculator_menu(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Выберите действие', reply_markup=await calculator_menu_keyboard())


@dp.callback_query_handler(text='breakeven_point')
async def breakeven_point(call: CallbackQuery, state: FSMContext):
    await BreakEvenPointState.price.set()
    await call.message.answer('Введите цену')


@dp.message_handler(regexp=is_num_regex, state=BreakEvenPointState.price)
async def price_entered(message: Message, state: FSMContext):
    await state.update_data(price=float(message.text))
    await BreakEvenPointState.next()
    await message.answer('Введите переменные издержки на единицу продукции')

@dp.message_handler(regexp=is_num_regex, state=BreakEvenPointState.avc)
async def avc_entered(message: Message, state: FSMContext):
    await state.update_data(avc=float(message.text))
    await BreakEvenPointState.next()
    await message.answer('Введите постоянные издержки без учета инвестиций в мес, руб')


@dp.message_handler(regexp=is_num_regex, state=BreakEvenPointState.tfc)
async def tfc_entered(message: Message, state: FSMContext):
    await state.update_data(tfc=float(message.text))
    await BreakEvenPointState.next()
    await message.answer('Введите срок амортизации, мес.')


@dp.message_handler(regexp=is_num_regex, state=BreakEvenPointState.amort)
async def amort_entered(message: Message, state: FSMContext):
    await state.update_data(amort=float(message.text))
    await BreakEvenPointState.next()
    await message.answer('Введите Инвестиционные издержки всего')


@dp.message_handler(regexp=is_num_regex, state=BreakEvenPointState.inv_all)
async def inv_all_entered(message: Message, state: FSMContext):
    await state.update_data(inv_all=float(message.text))
    data = await state.get_data()
    print(data)
    data['inv_month'] = data['inv_all'] / data['amort']
    data['fix_month'] = data['tfc'] + data['inv_month']
    data['breakeven_point'] = data['fix_month'] / (data['price'] - data['avc'])
    msg = f'''
Инвестиционные издержки в расчете на мес. - {data['inv_month']}
Постоянные издержки с учетом инвестиций в мес - {data['fix_month']}
Точка безубыточности, шт - {data['breakeven_point']}
'''
    await message.answer(msg)
    await state.finish()
