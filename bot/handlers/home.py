from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.misc import dp, bot


@dp.message_handler(text=['/start'], state='*')
async def start(message: Message):
    await message.answer('Добро пожаловать')
