# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:51:22 2018

@author: hjanssen
"""
from ripple_data import RippleAPI
from urllib.parse import urljoin


class RippleGateway(RippleAPI):
    """
    """

    GATEWAYS_URL = 'v2/gateways/{gateway}/'

    def __init__(self, gateway):
        self.gateway = gateway

    def __str__(self):
        return self.GATEWAYS_URL.format(**self.__dict__)

    @classmethod
    def gateways(cls):
        """
        Get information about known gateways.
        """

        return RippleAPI.get_ripple_data(
                urljoin(cls.GATEWAYS_URL.format(gateway=''), ''))

    def get(self):
        """
        Get information about a specific gateway from the Data API's list of
        known gateways.
        """

        return RippleAPI.get_ripple_data(urljoin(str(self), ''))
