import unittest2 as unittest
from oaxaca.policy.testing import OAXACA_POLICY_INTEGRATION_TESTING

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = OAXACA_POLICY_INTEGRATION_TESTING
    
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual("Oaxaca en Vivo", portal.getProperty('title'))
    
    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual("Bienvenido a Oaxaca en Vivo", portal.getProperty('description'))
