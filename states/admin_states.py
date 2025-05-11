from aiogram.fsm.state import State, StatesGroup

class AddChanel(StatesGroup):
    add_chanel = State()
    delete_chanel = State()