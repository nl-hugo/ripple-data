# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import currencies


class TestCurrencies(TestCase):

    def setUp(self):
        self.CURRENCY = 'XRP.svg'
        self.currency = currencies.RippleCurrency(self.CURRENCY)
        pass

    def test_str(self):
        self.assertEqual(str(self.currency),
                         'v2/currencies/{}/'.format(self.CURRENCY))

    def test_get(self):
        self.assertEqual(self.currency.get().headers['Content-Type'],
                         'image/svg+xml')
