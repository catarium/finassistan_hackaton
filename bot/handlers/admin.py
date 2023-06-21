from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.config import config
from bot.core.constants import is_num_regex, is_int_regex
from bot.db.models import Expense, User, Income, Category
from bot.handlers.keyboards.finances_menu_keyboard import \
    finances_menu_keyboard
from bot.handlers.keyboards.categories_keyboard import categories_keyboard
from bot.handlers.states.admin import AdminState
from bot.handlers.states.create_category import CreateCategoryState
from bot.handlers.states.delete_cateogory import DeleteCategoryState
from bot.misc import dp


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


