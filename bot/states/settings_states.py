from aiogram.fsm.state import State, StatesGroup

class SettingsStates(StatesGroup):
    START = State()
    SET_DELAY = State()
    SET_RESOURCES = State()