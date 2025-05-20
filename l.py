from ledgerblue.comm import getDongle
from web3 import Web3

# Connect to Ledger
dongle = getDongle(True)

# APDU command example to get Ethereum address (simplified)
# You need to build the correct APDU command for your derivation path
apdu_command = bytes.fromhex("e002000015058000002c8000003c8000000000000000")
dongle.exchange(apdu_command)  # Returns public key and address

# Use web3.py to build a transaction
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_ID'))
tx = {
    'nonce': w3.eth.getTransactionCount(address),
    'to': '0xRecipientAddress',
    'value': w3.toWei(0.01, 'ether'),
    'gas': 21000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'chainId': 1
}
signed_tx = ... # Send tx to Ledger for signing, get signature

# Broadcast signed transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Transaction sent with hash: {tx_hash.hex()}")
