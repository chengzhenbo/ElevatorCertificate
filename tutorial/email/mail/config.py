from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr

class Settings(BaseSettings):

    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_FROM_NAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr

    model_config = SettingsConfigDict(env_file="./.mailenv")


settings = Settings()