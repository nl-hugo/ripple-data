# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:53:57 2018

@author: hjanssen
"""
import requests
from urllib.parse import urlencode, urljoin


class RippleAPI(object):

    RIPPLE_API_URL = 'https://data.ripple.com/'
    MIME_TYPE_JSON = 'application/json; charset=utf-8'

    def __init__(self, address):
        self.address = address

    def get_ripple_data(self, method, params={}):
        """
        """
        # removes empty args
        query = dict((k, v) for k, v in params.items() if v)

        url_endpoint = urljoin(self.RIPPLE_API_URL, method)
        # print(url_endpoint)

        response = requests.get(url_endpoint, params=urlencode(query))
        # print(response.url)
        # print(response.headers['content-type'])

        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        if response.headers['content-type'] == self.MIME_TYPE_JSON:
            return response.json()

#        if response.headers['content-type'] == 'image/svg+xml':
#            return response

        return response
