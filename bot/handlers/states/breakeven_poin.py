from aiogram.dispatcher.filters.state import StatesGroup, State


class BreakEvenPointState(StatesGroup):
    price = State()
    avc = State()
    tfc = State()
    amort = State()
    inv_all = State()
