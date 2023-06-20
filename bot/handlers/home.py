from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.handlers.keyboards.home_keyboard import home_keyboard
from bot.misc import dp, bot


@dp.message_handler(text=['/start'], state='*')
async def start(message: Message):
    await message.answer('Добро пожаловать',
                         reply_markup=(await home_keyboard()))


@dp.callback_query_handler(text='home')
async def go_home(call: CallbackQuery):
    await call.message.delete()
    await start(call.message)
