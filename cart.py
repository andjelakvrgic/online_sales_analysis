class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_amount(self):
        return sum(item.price * item.quantity for item in self.cart_items)
    
    def show_cart(self):
        for item in self.cart_items:
            print(f"{item.name} -{item.quantity} * {item.price}")
        print(f"Total: {self.total_amount()}")