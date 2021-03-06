"""sample test"""
import unittest

from hello import hello


class TestHelloTcs(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world1'), 'hello world1')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_mybot(self):
        """sample test with new changes"""
        self.assertEqual(hello('bot'), 'hello bot')

    def test_fun(self):
        """sample test with additional changes"""
        self.assertEqual(hello('fun'), 'hello fun')

