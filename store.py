import products
from products import Product


class Store:

    def __init__(self, products:list[Product] = None):
        self.products: list[Product] = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity:int = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list:list[tuple[Product, int]]) -> float:
        order_total: float = 0
        for product, quantity in shopping_list:
            if product.is_active():
                order_total += product.buy(quantity)
        return order_total



#Testcase
# bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = products.Product("MacBook Air M2", price=1450, quantity=100)
#
# best_buy = Store([bose, mac])
# price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
# print(f"Order cost: {price} dollars.")