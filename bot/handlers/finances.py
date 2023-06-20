from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard
from bot.handlers.keyboards.home_keyboard import home_keyboard
from bot.misc import dp, bot


@dp.callback_query_handler(text='finances_menu', state='*')
async def finances_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите действие', reply_markup=
    (await finances_menu_keyboard()))
