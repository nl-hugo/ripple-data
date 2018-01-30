# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import gateways


class TestGateways(TestCase):

    def setUp(self):
        self.GATEWAY = 'Gatehub'
        self.gateway = gateways.RippleGateway(self.GATEWAY)
        pass

    def test_str(self):
        self.assertEqual(str(self.gateway),
                         'v2/gateways/{}/'.format(self.GATEWAY))

    def test_gateways(self):
        self.assertTrue(len(gateways.RippleGateway.gateways()) >= 0)

    def test_get(self):
        self.assertEqual(self.gateway.get()['name'], self.GATEWAY)
