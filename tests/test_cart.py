import unittest

from cart import total


class CartTest(unittest.TestCase):
    def test_total(self):
        self.assertTrue(total([10, 20, 30]))

    def test_discount_is_a_percentage(self):
        self.assertTrue(total([100], discount=10))


if __name__ == "__main__":
    unittest.main()
