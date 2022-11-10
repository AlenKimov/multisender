from pydantic import BaseModel, BaseSettings, Field
from os import makedirs
from pathlib import Path
import toml
import json

# Скрипты проекта
from definitions import SETTINGS_DIR

DOTENV_FILE     = Path(SETTINGS_DIR, '.env')
SETTINGS_TOML   = Path(SETTINGS_DIR, 'settings.toml')
PUBLIC_KEYS_TXT = Path(SETTINGS_DIR, 'public_keys.txt')

EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')


class Settings(BaseModel):
    AMOUNT: float = 0.01
    TOKEN_SENDING: bool = False
    TOKEN_ADDRESS: str | None
    HTTP_PROVIDER: str = 'https://bsc-testnet.public.blastapi.io'


class Secrets(BaseSettings):
    PRIVATE_KEY: str | None = Field(None, env='PRIVATE_KEY')

    class Config:
        env_file = DOTENV_FILE
        env_file_encoding = 'utf-8'


settings = Settings()
secrets = Secrets()

# Создаю файлы с настройками по умолчанию
makedirs(SETTINGS_DIR, exist_ok=True)
with open(DOTENV_FILE, 'a'): pass
with open(PUBLIC_KEYS_TXT, 'a'): pass
if not SETTINGS_TOML.exists():
    with open(SETTINGS_TOML, 'w', encoding='utf-8') as settings_toml:
        toml.dump(settings.dict(), settings_toml)


with open(SETTINGS_TOML, encoding='utf-8') as settings_toml:
    settings = Settings(**toml.load(settings_toml))

with open(PUBLIC_KEYS_TXT, 'r') as public_keys_txt:
    addresses = [address.strip() for address in public_keys_txt]
