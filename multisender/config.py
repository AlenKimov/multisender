from pydantic import BaseModel, BaseSettings, SecretStr, Field
import toml

from definitions import PROVIDERS_TOML, SETTINGS_TOML, PUBLIC_KEYS_TXT, DOTENV_FILE


class HttpProvider(BaseModel):
    BSC_MAINNET: str = "https://bsc-dataseed.binance.org/"
    BSC_TESTNET: str = "https://bsc-testnet.public.blastapi.io"


class Settings(BaseModel):
    amount: float


class Secrets(BaseSettings):
    ETH_MAINNET_HTTP_PROVIDER: str
    PRIVATE_KEY: str

    class Config:
        env_file = DOTENV_FILE
        env_file_encoding = 'utf-8'
        fields = {
            'ETH_MAINNET_HTTP_PROVIDER': {'env': 'ETH_MAINNET_HTTP_PROVIDER'},
            'PRIVATE_KEY': {'env': 'PRIVATE_KEY'}
        }


with open(PROVIDERS_TOML, encoding="utf-8") as toml_settings_file:
    providers_dict = toml.load(toml_settings_file)

with open(SETTINGS_TOML, encoding="utf-8") as toml_settings_file:
    settings_dict = toml.load(toml_settings_file)

providers = HttpProvider(**providers_dict)
settings = Settings(**settings_dict)
secrets = Secrets()

with open(PUBLIC_KEYS_TXT, "r") as file:
    addresses: list[str] = file.readlines()
    addresses = [address.strip() for address in addresses]


def save_settings():
    with open(SETTINGS_TOML, "w", encoding="utf-8") as settings_file:
        toml.dump(settings.dict(), settings_file)
