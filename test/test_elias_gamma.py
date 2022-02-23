import unittest

from algorithms.elias_gamma import EliasGammaCoder


class TestEliasGammaCoder(unittest.TestCase):
    def test_rigorously_integers(self):
        coder = EliasGammaCoder()
        for n in range(1, 10001):
            self.assertEqual(
                n,
                coder.decode(coder.encode(n)),
                f"Elias Gamma Coder failed for n  = {n}",
            )


if __name__ == "__main__":
    unittest.main()
