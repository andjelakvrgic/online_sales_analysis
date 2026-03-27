from product_manager import ProductManager
from product import Product
from cart import Cart

pm = ProductManager()

pm.add_product(Product("Laptop", 1200, 5))
pm.add_product(Product("Mouse", 25, 50))
pm.add_product(Product("Keyboard", 45, 30))

cart = Cart()
cart.add_product(pm.products[0])
cart.add_product(pm.products[1])
cart.add_product(pm.products[2])

cart.show_cart()

pm.show_products()

print("Total inventory value:", pm.total_value())