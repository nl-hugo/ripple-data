# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import ripple_api


class TestRippleAPI(TestCase):

    def test_get_ripple_data(self):
        version = ripple_api.RippleAPI.get_ripple_data('v2').json()['version']
        self.assertTrue(version.startswith('2'))

    def test_get_ripple_data_cannot_get(self):
        with self.assertRaisesRegex(ValueError, 'Cannot GET /v3'):
            ripple_api.RippleAPI.get_ripple_data('v3')
