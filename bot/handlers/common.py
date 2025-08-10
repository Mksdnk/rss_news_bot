import asyncio
from aiogram import Router
from aiogram.filters import CommandStart, Command
from bot.keyboards import admin
from aiogram.fsm.context import FSMContext
from bot.states.settings_states import SettingsStates
from aiogram.types import Message
from bot.handlers.sender import start_scheduler


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в бот! Он позволит производить рассылку новостей в тг-канал. Напишите /help для получения информации о том, как использовать бота.")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Для работы бота добавьте его в телеграм канал. Из админ панели с помощью комманды /settings вы можете управлять источниками, периодичностью отправки.")

@router.message(Command("settings"))
async def settings(message: Message, state: FSMContext):
    await message.answer("⚙️ Админ панель", reply_markup= await admin.admin_panel_keyboard())
    await state.set_state(SettingsStates.START)

@router.message(Command("start_sender"))
async def start_sender(message: Message):
    await message.answer("Рассылка началась")
    await start_scheduler()