

Python API for connecting to the Ripple DATA API. See the Ripple [API Method Reference](https://ripple.com/build/data-api-v2/). Currently implements the following API methods:

#### Ledger Contents Methods:
- Get Exchanges - GET /v2/exchanges/{:base}/{:counter}

#### Account Methods:
- Get Accounts - GET /v2/accounts
- Get Account - GET /v2/accounts/{:address}
- Get Account Balances - GET /v2/accounts/{:address}/balances
- Get Account Orders - GET /v2/accounts/{:address}/orders
- Get Account Transaction History - GET /v2/accounts/{:address}/transactions
- Get Account Payments - GET /v2/accounts/{:address}/payments
- Get Account Exchanges - GET /v2/accounts/{:address}/exchanges
- Get Account Balance Changes - GET /v2/accounts/{:address}/balance_changes
- Get Account Reports - GET /v2/accounts/{:address}/reports
- Get Account Transaction Stats - GET /v2/accounts/{:address}/stats/transactions
- Get Account Value Stats - GET /v2/accounts/{:address}/stats/value

TODO:
- Get Transaction By Account and Sequence - GET /v2/accounts/{:address}/transactions/{:sequence}

#### External Information Methods:
- Get All Gateways - GET /v2/gateways
- Get Gateway - GET /v2/gateways/{:gateway}
- Get Currency Image - GET /v2/currencies/{:currencyimage}
- Get rippled Versions - GET /v2/network/rippled_versions


## Installation
To install type
```
python install ripple_data
```

## Usage examples

**Current balance**

```python
from ripple_data import accounts

wallet = accounts.RippleAccount('rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn')
wallet.balances(currency='XRP')

#[{'currency': 'XRP', 'value': '86.106927'}]
```

**Request balance changes**

```python
from ripple_data import accounts

wallet = accounts.RippleAccount('rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn')
wallet.balance_changes(start=start_date, limit=1)

#[{'amount_change': '13499.98',
#  'change_type': 'payment_destination',
#  'currency': 'XRP',
#  'executed_time': '2018-01-15T12:17:10Z',
#  'final_balance': '13586.086927',
#  'ledger_index': 35842313,
#  'node_index': 0,
#  'tx_hash': '17C2821317465BDCB7E9185BCAA2571497D8B4802CD8205988C54DC4A9AEAB7A',
#  'tx_index': 2}]
```

**List gateway properties**
```python
from ripple_data import gateways

gateways.RippleGateway('Gatehub').get()

#{'accounts': [{'address': 'rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq',
#   'currencies': {'EUR': {'featured': True}, 'USD': {'featured': True}}}],
# 'assets': ['logo.grayscale.svg', 'logo.svg'],
# 'domain': 'gatehub.net',
# 'hotwallets': ['rhotcWYdfn6qxhVMbPKGDF3XCKqwXar5J4'],
# 'name': 'Gatehub',
# 'normalized': 'gatehub',
# 'start_date': '2015-02-15T00:00:00Z'}
```

**List ripple versions**
```python
from ripple_data import network

network.RippleNetwork.rippled_versions()

#[{'date': '2018-01-30T00:00:00Z', 'repo': 'nightly', 'version': '0.90.0'},
# {'date': '2018-01-30T00:00:00Z', 'repo': 'stable', 'version': '0.81.0'},
# {'date': '2018-01-30T00:00:00Z', 'repo': 'unstable', 'version': '0.81.0'}]
```

## Test and deployment commands

To run all tests:
```
python setup.py test
```

Or to run a single module test:
```
python -m unittest test_accounts
```

To deploy
```
python setup.py sdist
twine upload dist/*
```
