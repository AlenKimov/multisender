from eth_account.account import LocalAccount
from web3.contract import Contract

# Скрипты проекта
from definitions import EIP20_ABI
from _web3 import web3
from logger import logger
import requests
import json


def transfer(amount: float,
             private_key: str,
             address: str,
             gas: int = 21_000) -> str:
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
    tx_hash = web3.toHex(tx_hash)
    return tx_hash


# def multisend_ether(amount: float,
#               private_key: str,
#               addresses: list[str],
#               **kwargs):
#     tx_hashes: list = list()
#     for address in addresses:
#         tx_hash = transfer(amount, private_key, address, **kwargs)
#         tx_hash = web3.toHex(tx_hash)
#         tx_hashes.append(tx_hash)
#     return tx_hashes


def multisend_ether(amount: float,
                    private_key: str,
                    addresses: list[str],
                    gas: int = 21_000
                    ) -> list[str]:
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


# ETH_MAINNET_API_ENDPOINT = 'https://api.etherscan.io/api'
# BSC_TESTNET_API_ENDPOINT = 'https://api-testnet.bscscan.com/api'
#
#
# def get_abi(contract_address: str) -> dict:
#     querystring = {
#         "module": "contract",
#         "action": "getabi",
#         "address": contract_address
#     }
#     response = requests.get(BSC_TESTNET_API_ENDPOINT, params=querystring)
#     response_json = response.json()
#     abi_json = json.loads(response_json['result'])
#     return abi_json


def multisend_token(contract_address: str,
                    amount: float,
                    private_key: str,
                    addresses: list[str],
                    gas: int = 70_000):
    contract: Contract = web3.eth.contract(contract_address, abi=EIP20_ABI)
    account: LocalAccount = web3.eth.account.from_key(private_key)

    first_nonce = web3.eth.get_transaction_count(account.address)
    tx_hashes = list()
    for address, nonce in zip(addresses, range(first_nonce, first_nonce + len(addresses))):
        tx = contract.functions.transfer(
            address,
            web3.toWei(amount, "ether")
        ).buildTransaction({
            'nonce': nonce,
            'gas': gas,
            'gasPrice': web3.eth.gas_price
        })
        signed_tx = account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_hash = web3.toHex(tx_hash)
        tx_hashes.append(tx_hash)
        logger.success(f"[nonce: {nonce}, tx_hash: {tx_hash}] Успешная транзакция")
    return tx_hashes
