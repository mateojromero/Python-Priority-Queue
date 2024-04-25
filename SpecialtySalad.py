from Salad import Salad

class SpecialtySalad(Salad):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if size == 'S':
            super().set_price(12.50)
        elif size == 'M':
            super().set_price(14.50)
        elif size == 'L':
            super().set_price(16.50)

    def get_salad_details(self):
        string = ''
        string += 'SPECIALTY SALAD\n'
        string += f'Size: {self.size}\n'
        string += f'Name: {self.name}\n'
        string += f'Price: ${self.price:.2f}\n'
        return string
