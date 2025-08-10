from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import CallbackQuery, Message
from bot.states.settings_states import SettingsStates
from aiogram.filters import Command, CommandObject
from bot.db.crud import add_source, delete_source, get_sources
from bot.keyboards.admin import admin_panel_keyboard
from bot.handlers import sender

router = Router()

delay = 1

@router.message(SettingsStates.START)
async def start_settings(message: Message, state: FSMContext):
    await message.answer("Выберите действие", reply_markup=await admin_panel_keyboard())

@router.callback_query(F.data == "edit_delay")
async def edit_delay(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Введите задержку между отправками постов в минутах")
    await state.set_state(SettingsStates.SET_DELAY)

@router.message(SettingsStates.SET_DELAY)
async def set_delay(message: Message, state: FSMContext):
    if (not message.text.isdigit()):
        await message.answer("🛑 Ошибка! Введите число")
    else:
        await message.answer("Задержка установлена")
        delay = int(message.text)
        await sender.update_scheduler()
        await state.set_state(SettingsStates.START)

@router.callback_query(F.data == "edit_sources")
async def edit_sources(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Шаблон для добавления: /add rss_ссылка_на_источник \n"
                                        "Шаблон для удаления: /remove rss_ссылка_на_источник\n"
                                        "Введите /show для отображения текущих источников\n"
                                        "Введите /done для выхода")
    await state.set_state(SettingsStates.SET_RESOURCES)

@router.message(SettingsStates.SET_RESOURCES, Command("add"))
async def add_resources(message: Message, ComandObj: CommandObject, state: FSMContext):
    if ComandObj.args is None:
        await message.answer("🛑 Ошибка! Не переданы аргументы")
        return 

    entities = await message.entities or []
    url = None
    for item in entities:
        if item.type == "url":
            url = item.extract_from(message.text)
            await add_source(url)
            break
    if url == None:
        await message.answer("🛑 Ошибка! Не найдена ссылка")

@router.message(SettingsStates.SET_RESOURCES, Command("remove"))
async def remove_sources(message: Message, ComandObj: CommandObject, state: FSMContext):
    if ComandObj.args is None:
        await message.answer("🛑 Ошибка! Не переданы аргументы")
        return 

    entities = await message.entities or []
    url = None
    for item in entities:
        if item.type == "url":
            url = item.extract_from(message.text)
            await delete_source(url)  
            break
    if url == None:
        await message.answer("🛑 Ошибка! Не найдена ссылка")

@router.message(SettingsStates.SET_RESOURCES, Command("show"))
async def show_sources(message: Message, state: FSMContext):
    sources = await get_sources()
    links = [s.link for s in sources]
    await message.answer("📢 Список источников:\n"
        "\n".join(links))

@router.message(SettingsStates.SET_RESOURCES, Command("done"))
async def exit_editing_sources(message: Message, state: FSMContext):
    await message.answer("✅ Редактирование завершено")
    await state.set_state(SettingsStates.START)

@router.callback_query(F.data == "exit")
async def exit_editing_sources(call: CallbackQuery, state: FSMContext):
    await call.message.answer("✅ Настройка завершена")
    await state.clear()
