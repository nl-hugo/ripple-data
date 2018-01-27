# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:05:24 2018

@author: hjanssen
"""
from ripple_data import RippleAPI
from urllib.parse import urljoin


class RippleAccount(RippleAPI):
    """
    """

    ACCOUNTS_URL = 'v2/accounts/{address}/'

    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.ACCOUNTS_URL.format(**self.__dict__)

    def get_account(self):
        """
        Get creation info for a specific ripple account
        """

        method = ''

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method))

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs['account_data']

    def balances(self, ledger_index='', ledger_hash='', date='', currency='',
                 counterparty='', limit='', fmt=''):
        """
        Get all balances held or owed by a specific XRP Ledger account.
        """

        method = 'balances'

        params = {
            'ledger_index': ledger_index,
            'ledger_hash': ledger_hash,
            'date': date,
            'currency': currency,
            'counterparty': counterparty,
            'limit': limit,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method),
                                       params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs[method]

    def orders(self, ledger_index='', ledger_hash='', date='', limit='',
               fmt=''):
        """
        Get orders in the order books, placed by a specific account. This does
        not return orders that have already been filled.
        """

        method = 'orders'

        params = {
            'ledger_index': ledger_index,
            'ledger_hash': ledger_hash,
            'date': date,
            'limit': limit,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method),
                                       params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs[method]

    def balance_changes(self, currency='', counterparty='', start='', end='',
                        desc='', limit='', marker='', fmt=''):
        """
        Retrieve Balance changes for a given account over time.
        """

        method = 'balance_changes'

        params = {
            'currency': currency,
            'counterparty': counterparty,
            'start': start,
            'end': end,
            'descending': desc,
            'limit': limit,
            'marker': marker,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method),
                                       params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs[method]

    def value_stats(self, start='', end='', desc='', limit='', marker='',
                    fmt=''):
        """
        Retrieve daily summaries of transaction activity for an account
        """

        method = 'stats/value'

        params = {
            'start': start,
            'end': end,
            'descending': desc,
            'limit': limit,
            'marker': marker,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method),
                                       params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs['rows']

    def transaction_stats(self, start='', end='', desc='', limit='', marker='',
                          fmt=''):
        """
        Retrieve daily summaries of transaction activity for an account
        """

        method = 'stats/transactions'

        params = {
            'start': start,
            'end': end,
            'descending': desc,
            'limit': limit,
            'marker': marker,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(self, urljoin(str(self), method),
                                       params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs['rows']
