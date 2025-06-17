# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str

    # разрешаем лишние переменные и указываем файл .env
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",        # <- главное добавление
    )

settings = Settings()
