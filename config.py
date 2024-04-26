from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    words_count: int
    api_hash: SecretStr
    api_id: SecretStr
    bot_token: SecretStr
    phone: str
    chat_id: int
    model_config = SettingsConfigDict(env_file='.env', secrets_dir='/var/run')
    

config = Config()