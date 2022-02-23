import unittest

from algorithms.golomb import GolombCoder


class TestGolombCoder(unittest.TestCase):
    def test_rigorously_integers(self):
        for b in range(1, 1001):
            coder = GolombCoder(b)
            for n in range(1, 1001):
                self.assertEqual(
                    n,
                    coder.decode(coder.encode(n)),
                    f"Golomb Coder failed for n  = {n} and b = {b}",
                )


if __name__ == "__main__":
    unittest.main()
