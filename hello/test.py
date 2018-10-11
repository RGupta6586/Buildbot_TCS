
"""sample test"""
         self.assertEqual(hello('world'), 'hello world')

     def test_world_bytes(self):
         """sample test with bytes"""
         self.assertEqual(hello(b'world'), b'hello world')

     def test_world_unicode(self):
         """sample test with unicode"""
         self.assertEqual(hello(u'world'), u'hello world')
         
     def test_world_bytes(self):
         """sample test with bytes"""
         self.assertEqual(hello(b'bot'), b'hello bot')
