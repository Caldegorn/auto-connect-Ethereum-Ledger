
# auto-connect-Ethereum-Ledger

Auto connect and interact with an Ethereum Ledger hardware wallet using Python.

## Overview

This project provides tools and scripts to automatically detect, connect, and interact with an Ethereum Ledger hardware wallet from Python. It enables you to retrieve wallet addresses, sign Ethereum transactions, and integrate Ledger hardware wallet functionality into Python-based workflows or applications.

## Features

- Auto-detect connected Ledger devices via USB
- Retrieve Ethereum public addresses from Ledger
- Build and sign Ethereum transactions using the Ledger device
- Broadcast signed transactions to the Ethereum network via Web3.py
- Useful for backend services, automation scripts, or custom wallet integrations

## Prerequisites

- Python 3.7 or higher
- A Ledger hardware wallet with the Ethereum app installed
- USB connection to the Ledger device
- Access to an Ethereum RPC endpoint (e.g., Infura, Alchemy, or local node)

## Installation

1. Clone the repository:

```
git clone https://github.com/Caldegorn/auto-connect-Ethereum-Ledger.git
cd auto-connect-Ethereum-Ledger
```

2. (Optional) Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

*(If `requirements.txt` is not available, install manually:)*

```
pip install web3 ledgerblue hidapi
```

## Usage

1. Connect your Ledger device via USB and unlock it.
2. Open the Ethereum app on your Ledger device.
3. Run the Python script to auto-detect the Ledger and interact with it:

```
python main.py
```

4. The script will:

- Detect the Ledger device automatically
- Retrieve the Ethereum address from the Ledger
- Allow you to build and sign transactions
- Broadcast signed transactions to the Ethereum network

## Example

```
from ledger_eth import LedgerEthereum
from web3 import Web3

# Connect to Ledger and get address
ledger = LedgerEthereum()
address = ledger.get_address()
print(f"Ledger Ethereum address: {address}")

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Build transaction
nonce = w3.eth.getTransactionCount(address)
tx = {
    'nonce': nonce,
    'to': '0xRecipientAddress',
    'value': w3.toWei(0.01, 'ether'),
    'gas': 21000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'chainId': 1
}

# Sign transaction with Ledger
signed_tx = ledger.sign_transaction(tx)

# Send signed transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Transaction sent with hash: {tx_hash.hex()}")
```

*Note:* The above example assumes the presence of a `LedgerEthereum` wrapper class handling device communication and transaction signing.

## Troubleshooting

- Ensure your Ledger device is unlocked and the Ethereum app is open.
- Make sure your Python environment has access to USB devices (on some OSes, you may need additional permissions).
- Verify your RPC endpoint URL and network connectivity.
- For detailed Ledger communication errors, consult the Ledger developer documentation.

## Contributing

Contributions and improvements are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

