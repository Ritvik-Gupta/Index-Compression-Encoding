import unittest
from collections import deque

import utils


class TestUitls(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(utils.zero(), deque([False]))


if __name__ == "__main__":
    unittest.main()
