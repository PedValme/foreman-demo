import unittest

from cart import total


class CartTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([10, 20, 30]), 60)

    def test_discount_is_a_percentage(self):
        self.assertEqual(total([100], discount=10), 90)

    def test_discount_boundaries_and_fractional_percentage(self):
        cases = [
            ([10, 20, 30], 0, 60),
            ([10, 20, 30], 25, 45),
            ([10, 20, 30], 100, 0),
            ([80], 12.5, 70),
            ([], 10, 0),
        ]
        for prices, discount, expected in cases:
            with self.subTest(prices=prices, discount=discount):
                self.assertEqual(total(prices, discount=discount), expected)


if __name__ == "__main__":
    unittest.main()
