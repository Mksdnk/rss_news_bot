import asyncio
from aiogram import Bot, Dispatcher
from bot.config_reader import config
from bot.middleware.throttling import ThrottlingMiddleware
from bot.utils.rss_client import RSSClient
from bot.handlers import common, settings
from bot.db.database import async_engine
from bot.handlers.sender import scheduler

async def main():
    try:
        parser_task = asyncio.create_task(rss_client.rss_parser())
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        if scheduler.running:
            scheduler.shutdown(wait=False)
        rss_client.iss = False
        await async_engine.dispose()
        await bot.close()

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()
rss_client = RSSClient()



dp.message.middleware(ThrottlingMiddleware(limit=1.0))
dp.include_routers(common.router, settings.router)

if __name__ == '__main__':
    asyncio.run(main())
