# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import currencies

import os


class TestCurrencies(TestCase):

    def removeFile(self, fname):
        try:
            os.remove(fname)
        except OSError:
            pass

    def setUp(self):
        self.CURRENCY = 'XRP.svg'
        self.currency = currencies.RippleCurrency(self.CURRENCY)
        self.removeFile(self.CURRENCY)
        pass

    def tearDown(self):
        self.removeFile(self.CURRENCY)
        pass

    def test_str(self):
        self.assertEqual(str(self.currency),
                         'v2/currencies/{}/'.format(self.CURRENCY))

    def test_currency_image(self):
        self.currency.currency_image()
        self.assertTrue(os.path.isfile(self.CURRENCY))
