from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.models import User
from bot.handlers.keyboards.home_keyboard import home_keyboard
from bot.misc import dp


@dp.message_handler(text=['/start'], state='*')
async def start(message: Message, state: FSMContext):
    await state.finish()
    if not await User.filter(telegram_id=message.from_user.id).first():
        await User(telegram_id=message.from_user.id).save()
    await message.answer('Добро пожаловать',
                         reply_markup=(await home_keyboard()))


@dp.callback_query_handler(text='home')
async def go_home(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await start(call.message, state)
