from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from bot.config_reader import config

async_engine = create_async_engine(config.DATABASE_URL)
async_session_factory = async_sessionmaker(bind=async_engine)

class Base(DeclarativeBase):
    pass


