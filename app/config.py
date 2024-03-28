from pydantic import model_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str | None = None

    @model_validator(mode='after')
    def get_database_url(self):
        self.DATABASE_URL = f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return self
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

