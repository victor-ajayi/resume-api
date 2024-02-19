from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra="ignore")

    DB_NAME: str
    DB_PASSWORD: str


@lru_cache
def get_settings():
    return Settings(_env_file=".env")


settings = get_settings()
