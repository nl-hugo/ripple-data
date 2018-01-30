# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:05:24 2018

@author: hjanssen
"""
import sys

from ripple_data import RippleAPI


class RippleExchange(RippleAPI):
    """
    """

    EXCHANGES_URL = '/v2/exchanges/{base}/{counter}'

    def __init__(self, base, counter):
        self.base = base
        self.counter = counter

    def __str__(self):
        return self.EXCHANGES_URL.format(**self.__dict__)

    def exchanges(self, start='', end='', interval='', descending='',
                  reduce='', limit='', marker='', autobridged='', format=''):
        """
        Retrieve Exchanges for a given currency pair over time. Results can be
        returned as individual exchanges or aggregated to a specific list of
        intervals
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(str(self), locals())

        return result[method]
