from bot.db.crud import get_last_news
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.config_reader import config
from bot.handlers.settings import delay
import asyncio
import aiogram

scheduler = AsyncIOScheduler()
bot = aiogram.Bot(token=config.BOT_TOKEN)

async def start_scheduler():
    scheduler.start()

async def send_news():
    news = await get_last_news()
    if news:
        try:
            await bot.send_message(config.CHANNEL_ID, f"{news['title']}\n{news['description']}\n{news["link"]}")
        except aiogram.exceptions.TelegramAPIError:
            await asyncio.sleep(30)
    else:
        await bot.send_message(config.CHANNEL_ID, "No news found")
        await asyncio.sleep(60)

async def update_scheduler():
    scheduler.remove_all_jobs()
    scheduler.add_job(send_news, 'interval', minutes=delay, timezone="Europe/Moscow")

scheduler.add_job(send_news, 'interval', minutes=delay, timezone="Europe/Moscow")