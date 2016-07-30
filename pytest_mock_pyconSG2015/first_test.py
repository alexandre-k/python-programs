import unittest
from first_prog import plusone, f

class MyTest(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(plusone(3),4)

    def test_wrong_answer(self):
        self.assertFalse(plusone(3)==5)

    def test_f(self):
        self.assertRaises(SystemExit, f(), 'SystemExit: 1')
