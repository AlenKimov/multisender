from web3 import Web3

# Скрипты проекта
from logger import logger
from config import settings

web3 = Web3(Web3.HTTPProvider(settings.HTTP_PROVIDER))
logger.info(f"Connected to blockchain, chain id is {web3.eth.chain_id}.")
