from product_manager import ProductManager
from product import Product

pm = ProductManager()

pm.add_product(Product("Laptop", 1200, 5))
pm.add_product(Product("Mouse", 25, 50))
pm.add_product(Product("Keyboard", 45, 30))

pm.show_products()

print("Total inventory value:", pm.total_value())