from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    ESTAMP_PATH: str
    ESTAMP_XIZHI: str
    PDF_PATH: str


    model_config = SettingsConfigDict(env_file="./.fenv")


settings = Settings()