# ripple-data
Python API for connecting to the Ripple DATA API

Currently implements the following API methods:

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

TODO:
- Get rippled Versions - GET /v2/network/rippled_versions

## usage

### test

Run all tests:
```
python setup.py test
```

Or run a single module test:
```
python -m unittest test_accounts
```

### deploy
```
python setup.py sdist
twine upload dist/*
```

### install
```
python install ripple_data
```

## TODO

- extended tests
- code coverage
- argument checking?
- implement logging
