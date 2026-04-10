from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent 
env_file = BASE_DIR / ".env"


class EnvSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=env_file)


class Settings(BaseSettings):
    env: EnvSettings = EnvSettings()


settings = Settings()