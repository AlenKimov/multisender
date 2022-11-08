from web3 import Web3

# Скрипты проекта
from config import providers
from logger import logger

web3 = Web3(Web3.HTTPProvider(providers.BSC_TESTNET))
logger.info(f"Connected to blockchain, chain id is {web3.eth.chain_id}.")
