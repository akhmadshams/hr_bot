
from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalState(StatesGroup):
    name = State()
    b_date = State()
    phone = State()
    region = State()
    address = State()
    degree = State()
    old_work = State()
    position = State()
    additions = State()
    confirm = State()


