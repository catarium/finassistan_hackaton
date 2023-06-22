from aiogram.dispatcher.filters.state import StatesGroup, State


class AdviceState(StatesGroup):
    content = State()
    mult = State()
