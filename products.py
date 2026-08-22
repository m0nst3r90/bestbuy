class Product:
    """Product class"""
    def __init__(self, name, price, quantity):
        """Initialize the product"""
        self.name:str = name
        self.price:float = price
        self.quantity:int = quantity
        self.active:bool = True

    def get_quantity(self):
        """Return the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product"""
        self.quantity = quantity

    def is_active(self):
        """Returns a bool indicating if the product is active"""
        return self.active

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self):
        """Prints out the product"""
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a quantity and return its price

        Raises:
            ValueError: If the quantity is too low or the product is not active"""
        if not self.is_active():
            raise ValueError("Product is not active")

        if quantity > self.quantity:
            raise ValueError("Quantity is too high")

        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()
        return quantity * self.price
