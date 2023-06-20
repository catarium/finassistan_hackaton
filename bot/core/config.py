from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_NAME: str
    POSTGRES_PORT: str
    POSTGRES_PASSWORD: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


config = Settings()