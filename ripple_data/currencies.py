# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:51:22 2018

@author: hjanssen
"""
from ripple_data import RippleAPI
from urllib.parse import urljoin


class RippleCurrency(RippleAPI):
    """
    """

    CURRENCIES_URL = 'v2/currencies/{currencyimage}/'

    def __init__(self, currencyimage):
        self.currencyimage = currencyimage

    def __str__(self):
        return self.CURRENCIES_URL.format(**self.__dict__)

    def get(self):
        """
        Retrieve vector icons for various currencies.
        """

        return RippleAPI.get_ripple_data(urljoin(str(self), ''))
