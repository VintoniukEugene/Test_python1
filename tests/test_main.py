import unittest
from main import add
class TestMain (unittest. TestCase):
    def test_add (self):
        self. assertEqual(add(1, 2), 3)
        self. assertEqual(add(-1, 1), 0)
        self. assertEqual (add(0, 0), 0)
if __name__ == " main__":
    unittest.main()