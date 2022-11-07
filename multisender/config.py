from pydantic import BaseModel, BaseSettings, SecretStr, Field
import toml

from definitions import PROVIDERS_TOML, SETTINGS_TOML, PUBLIC_KEYS_TXT, DOTENV_FILE


class HttpProvider(BaseSettings):
    BSC_MAINNET: str = "https://bsc-dataseed.binance.org/"
    BSC_TESTNET: str = "https://bsc-testnet.public.blastapi.io"
    ETH_MAINNET: str | None = Field(None, env="ETH_MAINNET_HTTP_PROVIDER")

    class Config:
        env_file = DOTENV_FILE
        env_file_encoding = 'utf-8'


class Settings(BaseModel):
    token_sending: bool = False
    token_contract_address: str | None
    amount: float


class Secrets(BaseSettings):
    PRIVATE_KEY: str | None = Field(None, env="PRIVATE_KEY")

    class Config:
        env_file = DOTENV_FILE
        env_file_encoding = 'utf-8'


with open(PROVIDERS_TOML, encoding="utf-8") as providers_txt_file:
    providers_dict = toml.load(providers_txt_file)


with open(SETTINGS_TOML, encoding="utf-8") as settings_toml_file:
    settings_dict = toml.load(settings_toml_file)

providers = HttpProvider(**providers_dict)
settings = Settings(**settings_dict)
secrets = Secrets()

with open(PUBLIC_KEYS_TXT, "r") as file:
    addresses: list[str] = file.readlines()
    addresses = [address.strip() for address in addresses]


def save_settings():
    with open(SETTINGS_TOML, "w", encoding="utf-8") as settings_file:
        toml.dump(settings.dict(), settings_file)
