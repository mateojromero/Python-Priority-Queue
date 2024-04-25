from Salad import Salad

class SaladOrder:
    def __init__(self, time):
        self.time = time
        self.salads = []

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time
    
    def add_salad(self, salad):
        self.salads.append(salad)

    def info(self):
        string = f'***\nOrder Time: {self.time}\n'
        total_price = 0.0 
        for salad in self.salads:
            string += salad.get_salad_details() + '\n----\n'
            total_price += salad.get_price()
        string += f'TOTAL ORDER PRICE: ${total_price:.2f}\n***\n'
        return string
