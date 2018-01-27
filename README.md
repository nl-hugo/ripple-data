# ripple-data
Python API for connecting to the Ripple DATA API

Currently implements the following API methods:

#### Ledger Contents Methods:
- Get Exchanges - GET /v2/exchanges/{:base}/{:counter}

#### Account Methods:
- Get Account - GET /v2/accounts/{:address}
- Get Account Balances - GET /v2/accounts/{:address}/balances
- Get Account Orders - GET /v2/accounts/{:address}/orders
- Get Account Transaction Stats - GET /v2/accounts/{:address}/stats/transactions
- Get Account Value Stats - GET /v2/accounts/{:address}/stats/value

#### External Information Methods:
- Get Currency Image - GET /v2/currencies/{:currencyimage}

## usage

### test
```python setup.py test```


### deploy
```
python setup.py sdist
twine upload dist/*
```

### install
```python install ripple_data```
