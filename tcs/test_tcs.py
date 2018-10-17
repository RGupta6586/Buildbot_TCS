"""sample test"""
import unittest

from tcs import test


class NewTest(unittest.TestCase):
    """sample 465651 test"""

    def sum(self):
        """sample test"""
        a = 2;
        b = 3;
        self.assertEqual(test(a+b), 5)
