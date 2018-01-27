# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import exchanges


class TestExchanges(TestCase):

    def setUp(self):
        self.BASE = 'BTC+rchGBxcD1A1C2tdxF6papQYZ8kjRKMYcL'
        self.COUNTER = 'XRP+'
        self.exchange = exchanges.RippleExchange(self.BASE, self.COUNTER)
        pass

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(str(self.exchange),
                         '/v2/exchanges/{}/{}'.format(self.BASE, self.COUNTER))

    def test_get_exchanges(self):
        self.assertTrue(len(self.exchange.get_exchanges()) > 0)
        pass
