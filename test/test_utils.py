import unittest
from collections import deque

from  utils.binary_format import zero


class TestUitls(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(zero(), deque([False]))


if __name__ == "__main__":
    unittest.main()
