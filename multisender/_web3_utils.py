from eth_account.account import LocalAccount

# Скрипты проекта
from _web3 import web3
from logger import logger


def transfer(amount: float,
             private_key: str,
             address: str,
             gas: int = 21_000):
    account: LocalAccount = web3.eth.account.from_key(private_key)
    nonce = web3.eth.get_transaction_count(account.address)
    tx = {
        "nonce": nonce,
        "to": address,
        "value": web3.toWei(amount, "ether"),
        "gas": gas,
        "gasPrice": web3.toWei(40, "gwei")
    }

    signed_tx = account.sign_transaction(tx)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)


# def multisend(amount: float,
#               private_key: str,
#               addresses: list[str],
#               **kwargs):
#     tx_hashes: list = list()
#     for address in addresses:
#         tx_hash = transfer(amount, private_key, address, **kwargs)
#         tx_hash = web3.toHex(tx_hash)
#         tx_hashes.append(tx_hash)
#     return tx_hashes


def multisend(amount: float,
              private_key: str,
              addresses: list[str],
              gas: int = 21_000):
    tx_hashes: list = list()
    account: LocalAccount = web3.eth.account.from_key(private_key)
    first_nonce = web3.eth.get_transaction_count(account.address)
    for address, nonce in zip(addresses, range(first_nonce, first_nonce + len(addresses))):
        tx = {
            "nonce": nonce,
            "to": address,
            "value": web3.toWei(amount, "ether"),
            "gas": gas,
            "gasPrice": web3.toWei(40, "gwei")
        }
        signed_tx = account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_hash = web3.toHex(tx_hash)
        tx_hashes.append(tx_hash)
        logger.success(f"[nonce: {nonce}, tx_hash: {tx_hash}] Успешная транзакция")
    return tx_hashes
