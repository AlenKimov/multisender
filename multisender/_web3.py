from web3 import Web3

# Скрипты проекта
from config import providers

web3 = Web3(Web3.HTTPProvider(providers.BSC_TESTNET))
