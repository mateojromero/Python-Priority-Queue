
from Salad import Salad

class CustomSalad(Salad):
    def __init__(self, size):
        super().__init__(size)
        if size == 'S':
            super().set_price(8.75)
        elif size == 'M':
            super().set_price(10.75)
        elif size == 'L':
            super().set_price(12.75)
        self.toppings = []
        self.topping_prices = {'S': 1.75, 'M': 2.50, 'L': 3.00}

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += self.topping_prices[self.size]

    def get_salad_details(self):
        string = ''
        string += 'CUSTOM SALAD\n'
        string += f'Size: {self.size}\n'
        string += 'Toppings:\n'
        if self.toppings:
            for topping in self.toppings:
                string += f"\t+ {topping}\n"
        string += f"Price: ${self.price:.2f}\n"
        return string
    
