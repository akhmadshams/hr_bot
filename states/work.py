from aiogram.dispatcher.filters.state import StatesGroup, State

class WorkState(StatesGroup):
    title = State()
    body = State()
    image = State()
    salary = State()
    confirm = State()

class CategoryState(StatesGroup):
    title = State()
