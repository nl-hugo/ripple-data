# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:15:21 2018

@author: hjanssen
"""
from unittest import TestCase
from ripple_data import network


class TestNetwork(TestCase):

    def test_rippled_versions(self):
        self.assertTrue(len(network.RippleNetwork.rippled_versions()) >= 0)
