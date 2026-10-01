#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wifite2.tools.iwconfig import Iwconfig
from wifite2.tools.ifconfig import Ifconfig

import unittest

class TestDependency(unittest.TestCase):
    ''' Asserts "X or Y" dependencies check either program '''

    def testIwconfigOrIw(self):
        # Must not shell out to `which "iwconfig or iw"` literally
        self.assertTrue(Iwconfig.exists())

    def testIfconfigOrIp(self):
        self.assertTrue(Ifconfig.exists())

if __name__ == '__main__':
    unittest.main()
