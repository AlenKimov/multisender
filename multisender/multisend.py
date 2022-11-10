# Скрипты проекта
from logger import logger
from config import addresses, secrets, settings
from _web3 import web3
from _web3_utils import multisend_ether, multisend_token

addresses = [web3.toChecksumAddress(address) for address in addresses]


def multisend():
    if web3.isConnected():
        if settings.TOKEN_SENDING:
            multisend_token(settings.TOKEN_ADDRESS, settings.AMOUNT, secrets.PRIVATE_KEY, addresses)
        else:
            multisend_ether(settings.AMOUNT, secrets.PRIVATE_KEY, addresses)
    else:
        logger.error(f'[{web3.provider}] Нет подключения к RPC')
