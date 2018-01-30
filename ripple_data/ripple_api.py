# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:53:57 2018

@author: hjanssen
"""
import json
import requests
import logging

from urllib.parse import urlencode, urljoin

logger = logging.getLogger(__name__)


class RippleAPI(object):

    RIPPLE_API_URL = 'https://data.ripple.com/'
    MIME_TYPE_JSON = 'application/json; charset=utf-8'
    MIME_TYPE_TEXT = 'text/html; charset=utf-8'

    @classmethod
    def get_ripple_data(cls, method, params={}):
        """
        """

        logger.debug('Request method %s with params %s', method, params)

        # remove empty args
        try:
            del params['self']
            del params['method']
        except KeyError:
            pass
        query = dict((k, v) for k, v in params.items() if v)
        url_endpoint = urljoin(cls.RIPPLE_API_URL, method)

        # query
        response = requests.get(url_endpoint, params=urlencode(query))

        logger.info('GET [{}] {}'.format(response.status_code, response.url))

        # check response code
        if response.status_code != requests.codes.ok:
            json_data = response.json()
            if json_data and json_data['message']:
                raise ValueError(json_data['message'])
            else:
                response.raise_for_status()

        logger.debug('MIMETYPE {}'.format(response.headers['content-type']))

        # get data from response
        if response.headers['content-type'] == cls.MIME_TYPE_JSON:
            json_data = response.json()
            if "result" in json_data and json_data["result"] == "success":
                return json_data

        elif response.headers['content-type'] == cls.MIME_TYPE_TEXT:
            return json.loads(response.text)

        return response
