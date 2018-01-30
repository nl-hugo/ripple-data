# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:51:22 2018

@author: hjanssen
"""
from ripple_data import RippleAPI
from urllib.parse import urljoin


class RippleNetwork(RippleAPI):
    """
    """

    NETWORK_URL = 'v2/network/'

    @classmethod
    def rippled_versions(cls):
        """
       Reports the latest versions of rippled available from the official
       Ripple Yum repositories.
        """

        method = 'rippled_versions'
        result = RippleAPI.get_ripple_data(urljoin(cls.NETWORK_URL, method))

        return result['rows']
