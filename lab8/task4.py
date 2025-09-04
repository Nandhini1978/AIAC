class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, name, price):
        """Add an item with its price to the cart."""
        self.items[name] = price

    def remove_item(self, name):
        """Remove an item from the cart by name."""
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        """Return the total cost of all items in the cart."""
        return sum(self.items.values())
# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 2.0)
    cart.add_item("Milk", 3.25)
    print("Total cost:", cart.total_cost())
    cart.remove_item("Banana")
    print("Total cost after removing Banana:", cart.total_cost())