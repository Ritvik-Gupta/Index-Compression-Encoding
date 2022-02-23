import unittest

from algorithms.elias_delta import EliasDeltaCoder


class TestEliasDeltaCoder(unittest.TestCase):
    def test_rigorously_integers(self):
        coder = EliasDeltaCoder()
        for n in range(1, 10001):
            self.assertEqual(
                n,
                coder.decode(coder.encode(n)),
                f"Elias Delta Coder failed for n  = {n}",
            )


if __name__ == "__main__":
    unittest.main()
