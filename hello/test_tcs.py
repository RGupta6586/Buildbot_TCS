"""sample test"""
import unittest

from hello import test


class NewTest(unittest.TestCase):
    """sample test"""

    def sum(self):
        """sample test"""
        a = 2;
        b = 3;
        self.assertEqual(test(a+b), 5)
