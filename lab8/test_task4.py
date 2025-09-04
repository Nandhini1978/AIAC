import unittest
from task4 import ShoppingCart
class TestShoppingCartTotalCost(unittest.TestCase):
    def test_total_cost_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total_cost(), 0)
    def test_total_cost_single_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        self.assertEqual(cart.total_cost(), 1.5)
    def test_total_cost_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        cart.add_item("Banana", 2.0)
        cart.add_item("Milk", 3.25)
        self.assertEqual(cart.total_cost(), 6.75)
    def test_total_cost_after_removal(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        cart.add_item("Banana", 2.0)
        cart.remove_item("Banana")
        self.assertEqual(cart.total_cost(), 1.5)
    def test_total_cost_update_item_price(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        cart.add_item("Apple", 2.0)  # Updates price
        self.assertEqual(cart.total_cost(), 2.0)
if __name__ == "__main__":
    unittest.main()