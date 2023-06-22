from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.config import config
from bot.core.constants import is_num_regex, is_int_regex
from bot.db.models import Expense, User, Income, Category, Advice
from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard
from bot.handlers.keyboards.categories_keyboard import categories_keyboard
from bot.handlers.states.admin import AdminState
from bot.handlers.states.create_advice import AdviceState
from bot.handlers.states.create_category import CreateCategoryState
from bot.handlers.states.delete_advice import DeleteAdviceState
from bot.handlers.states.delete_cateogory import DeleteCategoryState
from bot.misc import dp

import re


@dp.message_handler(text=['/admin'], state='*')
async def get_admin(message: Message):
    await message.answer('Введите код')
    await AdminState.code.set()


@dp.message_handler(state=AdminState.code)
async def code_entered(message: Message):
    if message.text != config.ADMIN_CODE:
        await message.answer('Неверный код')
        return
    await AdminState.admin.set()
    await message.answer('Права администратора получены')


@dp.message_handler(text=['/categories'], state=AdminState.admin)
async def add_category(message: Message):
    categories = "\n".join([f'{c.id} {c.name}'for c in await Category.all()])
    msg = f'''
Категории:
{categories}
    '''
    await message.answer(msg)


@dp.message_handler(text=['/delete_category'], state=AdminState.admin)
async def delete_cateogory(message: Message):
    await message.answer('Введите id')
    await DeleteCategoryState.id.set()


@dp.message_handler(state=DeleteCategoryState.id, regexp=is_int_regex)
async def category_id_entered(message: Message, state: FSMContext):
    category = await Category.filter(id=int(message.text)).first()
    if not category:
        await message.answer('Категория не найдена')
        return
    await category.delete()
    await AdminState.admin.set()
    await message.answer('Категория удалена')


@dp.message_handler(text=['/add_category'], state=AdminState.admin)
async def add_category(message: Message):
    await message.answer('Введите название категории')
    await CreateCategoryState.name.set()


@dp.message_handler(state=CreateCategoryState.name)
async def category_name_entered(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await Category(**data).save()
    await message.answer('Категория добавлена')
    await AdminState.admin.set()


@dp.message_handler(text='/advices', state=AdminState.admin)
async def advices(message: Message, state: FSMContext):
    advices = '\n'.join([f'{advice.id} {advice.content}' for advice in await Advice.all()])
    msg = f'''
Советы:    
{advices}
'''
    if len(msg) > 4095:
        for x in range(0, len(msg), 4095):
            await message.answer(msg[x:x+4095])
    else:
        await message.answer(msg)


@dp.message_handler(text='/add_advice', state=AdminState.admin)
async def add_advice(message: Message, state: FSMContext):
    await message.answer('Введите совет')
    await AdviceState.content.set()


@dp.message_handler(state=AdviceState.content)
async def content_entered(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    data = await state.get_data()
    await save_advice(data, message)



async def save_advice(data, message):
    await Advice(**data).save()
    await message.answer('Совет добавлен')
    await AdminState.admin.set()

@dp.message_handler(text='/delete_advice', state=AdminState.admin)
async def delete_advice(message: Message, state: FSMContext):
    await message.answer("Введите id")
    await DeleteAdviceState.id.set()


@dp.message_handler(state=DeleteAdviceState.id)
async def advice_id_entered(message: Message, state: FSMContext):
    advice = await Advice.filter(id=int(message.text)).first()
    if not advice:
        await message.answer('Совет с таким id не найден')
        return
    await advice.delete()
    await AdminState.admin.set()
    await message.answer('Совет удален')


