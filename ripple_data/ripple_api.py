# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:53:57 2018

@author: hjanssen
"""
import json
import requests

from urllib.parse import urlencode, urljoin


class RippleAPI(object):

    RIPPLE_API_URL = 'https://data.ripple.com/'
    MIME_TYPE_JSON = 'application/json; charset=utf-8'
    MIME_TYPE_TEXT = 'text/html; charset=utf-8'

    @classmethod
    def get_ripple_data(cls, method, params={}):
        """
        """

        # removes empty args
        print('###')
        print(params)
        try:
            #del params['self'] # kan weg?
            del params['method']
        except KeyError:
            pass
        print('$$$')
        print(params)
        print(method)
        query = dict((k, v) for k, v in params.items() if v)

        url_endpoint = urljoin(cls.RIPPLE_API_URL, method)
        print(url_endpoint)

        response = requests.get(url_endpoint, params=urlencode(query))
        print(response)
        print(response.url)
        print(response.headers['content-type'])

#        json_data = response.json()

        if response.status_code != requests.codes.ok:
            # TODO: is this fool-proof?
            
            # first try to see if there is API message
            # raise ValueError(response.json()['message'])
            
            # else raise_for_status
            
            json_data = response.json()
            if json_data and json_data['message']:
                raise ValueError(json_data['message'])
            else:
                response.raise_for_status()

#       TODO: check result, but only for JSON
#        if response['result'] != 'success':
#            raise KeyError("{} not found".format(method))

        if response.headers['content-type'] == cls.MIME_TYPE_JSON:
            json_data = response.json()
            print(json_data)
            if "result" in json_data and json_data["result"] == "success":
                return json_data

        if response.headers['content-type'] == cls.MIME_TYPE_TEXT:
            json_data = response.text
            print(json_data)
            return json.loads(json_data)


#        if response.headers['content-type'] == 'image/svg+xml':
#            return response

        return response
