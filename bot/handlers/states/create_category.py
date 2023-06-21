from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateCategoryState(StatesGroup):
    name = State()
