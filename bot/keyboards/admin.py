import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def admin_panel_keyboard() -> InlineKeyboardMarkup:
    buttons =  [InlineKeyboardButton(text='🛠️ Редактировать источники', callback_data="edit_sources"),
                InlineKeyboardButton(text='⏱️ Насторить периодичность отправки', callback_data="edit_delay"),
                InlineKeyboardButton(text='⬅️ Назад', callback_data="exit")]
    builder = InlineKeyboardBuilder()
    for b in buttons:
        builder.add(b)
    
    builder.adjust(1)
    return builder.as_markup()