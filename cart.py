"""A tiny shopping cart with one bug, for trying Foreman.

`discount` is a percentage (10 means 10 %).
"""


def total(prices, discount=0):
    """The sum of `prices`, less `discount` percent."""
    return sum(prices) * (100 - discount) / 100
