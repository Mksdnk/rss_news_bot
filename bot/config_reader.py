from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, PostgresDsn,RedisDsn, SecretStr, AnyUrl

from typing import Annotated

class Settings(BaseSettings):
    # Database settings
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str 
    POSTGRES_HOST: str 
    POSTGRES_PORT: int 

    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    

    # Redis settings
    #REDIS_HOST: RedisDsn 

    #Telegram settings
    BOT_TOKEN: str 

    # open ai
    CHAT_GPT_API_KEY: SecretStr

    CHANNEL_ID: int
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

config = Settings()

    