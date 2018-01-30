# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:05:24 2018

@author: hjanssen
"""
import sys

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

    @classmethod
    def accounts(cls):
        """
        Get info for all account creations.
        """

        method = 'accounts'
        result = RippleAPI.get_ripple_data(
                urljoin(cls.ACCOUNTS_URL.format(address=''), ''))

        return result[method]

    def get(self):
        """
        Get creation info for a specific ripple account.
        """

        method = ''
        result = RippleAPI.get_ripple_data(urljoin(str(self), method))

        return result['account_data']

    def balances(self, ledger_index='', ledger_hash='', date='', currency='',
                 counterparty='', limit='', format=''):
        """
        Get all balances held or owed by a specific XRP Ledger account.
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def orders(self, ledger_index='', ledger_hash='', date='', limit='',
               format=''):
        """
        Get orders in the order books, placed by a specific account. This does
        not return orders that have already been filled.
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def transactions(self, start='', end='', min_sequence='', max_sequence='',
                     type='', result='', binary='', descending='', limit='',
                     format=''):
        """
        Retrieve a history of transactions that affected a specific account.
        This includes all transactions the account sent, payments the account
        received, and payments that rippled through the account.
        """
        # TODO: sequence implementation

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def payments(self, start='', end='', type='', currency='', issuer='',
                 source_tag='', destination_tag='', descending='', limit='',
                 marker='', format=''):
        """
        Retrieve a payments for a specified account.
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def exchanges(self, base='', counter='', start='', end='', type='',
                  descending='', limit='', marker='', format=''):
        """
        Retrieve Exchanges for a given account over time.
        """
        # TODO: base, counter implementation

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def balance_changes(self, currency='', counterparty='', start='', end='',
                        descending='', limit='', marker='', format=''):
        """
        Retrieve Balance changes for a given account over time.
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def reports(self, currency='', counterparty='', date='', start='', end='',
                accounts='', payments='', descending='', format=''):
        """
        Retrieve daily summaries of payment activity for an account.
        """
        # TODO: check date OR start and end

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result[method]

    def value_stats(self, start='', end='', descending='', limit='', marker='',
                    format=''):
        """
        Retrieve daily summaries of transaction activity for an account.
        """

        method = 'stats/value'
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result['rows']

    def transaction_stats(self, start='', end='', descending='', limit='',
                          marker='', format=''):
        """
        Retrieve daily summaries of transaction activity for an account.
        """

        method = 'stats/value'
        result = RippleAPI.get_ripple_data(urljoin(str(self), method),
                                           locals())

        return result['rows']
