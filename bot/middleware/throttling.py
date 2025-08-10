import time
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Any

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=0.5):
        self.limit = limit
        self.last_time = {}

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        current_time = time.time()

        if user_id in self.last_time:
            elapsed = current_time - self.last_time[user_id]
            if elapsed < self.limit:
                await event.answer("⏳ Слишком много запросов! Подождите немного.")
                return
        self.last_time[user_id] = current_time
        return await handler(event, data)