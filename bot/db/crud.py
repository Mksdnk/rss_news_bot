from bot.db.database import Base, async_session_factory, async_engine
from bot.db.models import News, Sources
from sqlalchemy import delete, select, func, update
import asyncio

# async def create_tables():
#     async with async_engine.begin() as conn:
#         conn.echo = True
#         await conn.run_sync(Base.metadata.drop_all(async_engine))
#         await conn.run_sync(Base.metadata.create_all(async_engine))
#         conn.echo = True

async def add_news(title: str, description: str, link: str):
    async with async_session_factory() as session:
        news = News(title=title, description=description, link = link)
        session.add(news)
        await session.commit()
        await session.refresh(news)
        await session.commit()

async def get_last_news():
    async with async_session_factory() as session:
        stmt = select(News).where(News.is_sent == False).order_by(News.id.desc()).limit(1)
        result = await session.execute(stmt)
        last_news = result.scalars().first()
        if not last_news:
            return None
        stmt = update(News).where(News.id == last_news.id).values(is_sent=True)
        await session.execute(stmt)
        news_data = {
            "title": last_news.title,
            "description": last_news.description,
            "link": last_news.link
        }
        await session.commit()
        return news_data
    
async def add_source(source: str):
    async with async_session_factory() as session:
        source_ = Sources(link=source)
        session.add(source_)
        await session.commit()
        await session.refresh(source_)
        await session.commit()

async def get_sources():
    async with async_session_factory() as session:
        stmt = select(Sources)
        result = await session.execute(stmt)
        sources = result.scalars().all()
        return sources
    
async def delete_source(source: str):
    async with async_session_factory() as session:
        stmt = delete(Sources).where(Sources.link == source)
        await session.execute(stmt)
        await session.commit()

async def count_sources():
    async with async_session_factory() as session:
        stmt = select(func.count(Sources.id))
        result = await session.execute(stmt)
        count = result.scalar()
        return count

