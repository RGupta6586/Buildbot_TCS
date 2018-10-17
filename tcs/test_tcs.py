"""sample test"""
import unittest

from tcs import tcs


class NewTest(unittest.TestCase):
    """sample 465651 test"""

    def sum(self):
        """sample test"""
        a = 2;
        b = 3;
        self.assertEqual(tcs(a+b), 5)
