import unittest

class SampleTetst(unittest.TestCase):

    def test1(self):
        self.assertEqual(5,5)

    def test2(self):
        self.assertEqual(5, 6)

    def test3(self):
        self.assertEqual(5, 5)

if __name__ == '__main__':
    unittest.main()

