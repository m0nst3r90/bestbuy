class Product:
    def __init__(self, name, price, quantity):
        self.name:str = name
        self.price:float = price
        self.quantity:int = quantity
        self.active:bool = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity += quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        try:
            if not self.is_active(): raise ValueError("Product is not active")

            if quantity > self.quantity:
                raise ValueError("Quantity is too high")
            else:
                self.quantity -= quantity
                return quantity * self.price
        except ValueError as e:
            print(e)


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()