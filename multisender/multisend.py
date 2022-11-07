# Скрипты проекта
from _web3 import web3
from _web3_utils import multisend as _multisend
from config import addresses, secrets, settings
from logger import logger

addresses = [web3.toChecksumAddress(address) for address in addresses]


def multisend():
    if web3.isConnected():
        _multisend(settings.amount, secrets.PRIVATE_KEY, addresses)
    else:
        logger.error(f'[{web3.provider}] Нет подключения к RPC')
