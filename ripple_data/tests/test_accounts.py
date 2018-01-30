# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import accounts


class TestAccounts(TestCase):
    """
    Tests 'happy flows' and arguments that may lead to a server error.

    This excludes testing arguments like 'descending', 'limit' and 'marker'
    which, if specified wrongly, will simply be ignored by the API.
    """

    def setUp(self):
        self.ADDRESS = 'rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn'
        self.account = accounts.RippleAccount(self.ADDRESS)
        pass

    def test_str(self):
        self.assertEqual(str(self.account),
                         'v2/accounts/{}/'.format(self.ADDRESS))

    def test_accounts(self):
        self.assertTrue(len(accounts.RippleAccount.accounts()) >= 0)

    def test_get(self):
        self.assertEqual(self.account.get()['account'], self.ADDRESS)

    def test_get_not_found(self):
        with self.assertRaisesRegex(ValueError, 'Account not found'):
            accounts.RippleAccount('not_there').get()

    def test_balances(self):
        self.assertTrue(len(self.account.balances()) >= 0)

    def test_balances_currency_invalid(self):
        self.assertTrue(len(self.account.balances(currency='invalid')) == 0)

    def test_orders(self):
        self.assertTrue(len(self.account.orders()) >= 0)

    def test_orders_ledger_index_invalid(self):
        with self.assertRaisesRegex(ValueError, 'unable to retrieve orders'):
            self.account.orders(ledger_index='invalid')

    def test_transactions(self):
        self.assertTrue(len(self.account.transactions()) >= 0)

    def test_transactions_min_sequence_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid min_sequence'):
            self.account.transactions(min_sequence='invalid')

    def test_transactions_max_sequence_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid max_sequence'):
            self.account.transactions(max_sequence='invalid')

    def test_transactions_type_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid transaction type'):
            self.account.transactions(type='invalid')

    def test_transactions_result_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid transaction result'):
            self.account.transactions(result='invalid')

    def test_payments(self):
        self.assertTrue(len(self.account.payments()) >= 0)

    def test_payments_start_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid start date format'):
            self.account.payments(start='invalid')

    def test_payments_end_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid end date format'):
            self.account.payments(end='invalid')

    def test_payments_type_invalid(self):
        with self.assertRaisesRegex(ValueError,
                                    'invalid type - use: sent, received'):
            self.account.payments(type='invalid')

    def test_exchanges(self):
        self.assertTrue(len(self.account.exchanges()) >= 0)

    def test_exchanges_start_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid start date format'):
            self.account.exchanges(start='invalid')

    def test_exchanges_end_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid end date format'):
            self.account.exchanges(end='invalid')

    def test_balance_changes(self):
        self.assertTrue(len(self.account.balance_changes()) >= 0)

    def test_balance_start_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid start date format'):
            self.account.balance_changes(start='invalid')

    def test_balance_end_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid end date format'):
            self.account.balance_changes(end='invalid')

    def test_reports(self):
        self.assertTrue(len(self.account.reports()) >= 0)

    def test_value_stats(self):
        self.assertTrue(len(self.account.value_stats()) >= 0)

    def test_value_stats_start_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid start date format'):
            self.account.value_stats(start='invalid')

    def test_value_stats_end_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid end date format'):
            self.account.value_stats(end='invalid')

    def test_transaction_stats(self):
        self.assertTrue(len(self.account.transaction_stats()) >= 0)

    def test_transaction_stats_start_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid start date format'):
            self.account.balance_changes(start='invalid')

    def test_transaction_stats_end_invalid(self):
        with self.assertRaisesRegex(ValueError, 'invalid end date format'):
            self.account.transaction_stats(end='invalid')
