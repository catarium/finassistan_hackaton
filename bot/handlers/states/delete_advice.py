from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteAdviceState(StatesGroup):
    id = State()
