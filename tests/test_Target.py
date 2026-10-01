#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wifite2.tools.airodump import Airodump

import unittest

class TestTarget(unittest.TestCase):
    ''' Test suite for Target parsing an generation '''

    airodump_csv = 'airodump.csv'

    def getTargets(self, filename):
        ''' Helper method to parse targets from filename '''
        import os, inspect
        this_file = os.path.abspath(inspect.getsourcefile(TestTarget.getTargets))
        this_dir = os.path.dirname(this_file)
        csv_file = os.path.join(this_dir, 'files', filename)
        # Load targets from CSV file
        return Airodump.get_targets_from_csv(csv_file)

    def testTargetParsing(self):
        ''' Asserts target parsing finds targets '''
        targets = self.getTargets(TestTarget.airodump_csv)
        assert(len(targets) > 0)

    def testTargetClients(self):
        ''' Asserts target parsing captures clients properly '''
        targets = self.getTargets(TestTarget.airodump_csv)
        for t in targets:
            if t.bssid == '00:1D:D5:9B:11:00':
                assert(len(t.clients) > 0)

    def testEnterprisePlain(self):
        ''' Stock airodump-ng (Authentication=MGT) parses as WPE '''
        targets = self.getTargets(TestTarget.airodump_csv)
        matches = [t for t in targets if t.bssid == '00:C0:CA:96:45:2F']
        assert(len(matches) == 1)
        assert(matches[0].encryption == 'WPE')
        assert(matches[0].eap_methods == [])
        assert(matches[0].encryption_tag() == 'WPE')

    def testEnterpriseMethod(self):
        ''' Patched airodump-ng (MGT+TEAP) parses method detail '''
        targets = self.getTargets(TestTarget.airodump_csv)
        matches = [t for t in targets if t.bssid == '00:17:9A:B7:AA:5B']
        assert(len(matches) == 1)
        assert(matches[0].encryption == 'WPE')
        assert(matches[0].eap_methods == ['TEAP'])
        assert(matches[0].encryption_tag() == 'WPE+TEAP')

    def testPersonalUnchanged(self):
        ''' PSK networks still parse as WPA '''
        targets = self.getTargets(TestTarget.airodump_csv)
        matches = [t for t in targets if t.bssid == '00:13:10:33:A6:56']
        assert(len(matches) == 1)
        assert(matches[0].encryption == 'WPA')
        assert(matches[0].eap_methods == [])

if __name__ == '__main__':
    unittest.main()
