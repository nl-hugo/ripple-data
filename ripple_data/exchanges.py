# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:05:24 2018

@author: hjanssen
"""
from ripple_data import RippleAPI
from urllib.parse import urljoin


class RippleExchange(RippleAPI):
    """
    """

    EXCHANGES_URL = '/v2/exchanges/{base}/{counter}'

    def __init__(self, base, counter):
        self.base = base
        self.counter = counter
        # TODO: validate? unless XRP, currency should have an issuer

    def __str__(self):
        return self.EXCHANGES_URL.format(**self.__dict__)

    def get_exchanges(self, start='', end='', interval='', desc='',
                      reduce='', limit='', marker='', autobridged='', fmt=''):
        """
        Retrieve Exchanges for a given currency pair over time.
        Results can be returned as individual exchanges or
        aggregated to a specific list of intervals
        """

        method = ''

        params = {
            'start': start,
            'end': end,
            'interval': interval,
            'descending': desc,
            'reduce': reduce,
            'limit': limit,
            'marker': marker,
            'autobridged': autobridged,
            'format': fmt
        }

        rs = RippleAPI.get_ripple_data(
                self, urljoin(str(self), method), params)

        if rs['result'] != 'success':
            raise KeyError("{} not found".format(method))

        return rs['exchanges']
