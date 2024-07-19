from main import suma
import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2,3), 5)
if __name__ == '__main__':
    unittest.main()