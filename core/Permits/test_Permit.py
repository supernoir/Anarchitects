import unittest

from core.Permits.Permit import Permit
from core.Permits.permittype import PermitType


class MyTestCase(unittest.TestCase):
    def setUp(self):
        try:
            permit = Permit(PermitType.BUILDING)
            print(permit)
            pass
        except:
            return AssertionError

    def test_cointoss(self):
        permit = Permit(PermitType.BUILDING)
        result = permit.cointoss()
        self.assertEqual(result, (True or False))


if __name__ == '__main__':
    unittest.main()
