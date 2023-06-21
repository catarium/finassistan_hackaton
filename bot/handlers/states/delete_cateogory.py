from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteCategoryState(StatesGroup):
    id = State()
