import unittest

from algorithms.unary import UnaryCoder


class TestUnaryCoder(unittest.TestCase):
    def test_rigorously_integers(self):
        coder = UnaryCoder()
        for n in range(1, 10001):
            self.assertEqual(
                n, coder.decode(coder.encode(n)), f"Unary Coder failed for n  = {n}"
            )


if __name__ == "__main__":
    unittest.main()
