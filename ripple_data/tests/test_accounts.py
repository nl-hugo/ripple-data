# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import accounts


class TestAccounts(TestCase):

    def setUp(self):
        self.ADDRESS = 'rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn'
        self.account = accounts.RippleAccount(self.ADDRESS)
        pass

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(str(self.account),
                         'v2/accounts/{}/'.format(self.ADDRESS))

    def test_account(self):
        self.assertEqual(self.account.account()['account'], self.ADDRESS)

    def test_balances(self):
        self.assertTrue(len(self.account.balances()) >= 0)

    def test_orders(self):
        self.assertTrue(len(self.account.orders()) >= 0)

    def test_transactions(self):
        self.assertTrue(len(self.account.transactions()) >= 0)

    def test_payments(self):
        self.assertTrue(len(self.account.payments()) >= 0)

    def test_exchanges(self):
        self.assertTrue(len(self.account.exchanges()) >= 0)

    def test_balance_changes(self):
        self.assertTrue(len(self.account.balance_changes()) >= 0)

    def test_reports(self):
        self.assertTrue(len(self.account.reports()) >= 0)

    def test_value_stats(self):
        self.assertTrue(len(self.account.value_stats()) >= 0)

    def test_transaction_stats(self):
        self.assertTrue(len(self.account.transaction_stats()) >= 0)
