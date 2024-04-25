from Salad import Salad
from CustomSalad import CustomSalad
from SpecialtySalad import SpecialtySalad
from SaladOrder import SaladOrder
import OrderQueue

class Test_Salad:

    def test_init(self):
        s1 = Salad('S')
        assert s1.get_price() == 0.0
        assert s1.get_size() == 'S'

    def test_get_price(self):
        s1 = Salad('S')
        s1.set_price(8.75)
        assert s1.get_price() == 8.75

    def test_set_price(self):
        s1 = Salad('S')
        s1.set_price(8.75)
        assert s1.get_price() == 8.75

    def test_get_size(self):
        s1 = Salad('M')
        assert s1.get_size() == 'M'

    def test_set_size(self):
        s1 = Salad('M')
        s1.set_size('S')
        assert s1.get_size() == 'S'

class Test_CustomSalad:

    def test_init(self):
        s1 = CustomSalad('L')
        assert s1.get_size() == 'L'
        assert s1.get_price() == 12.75
        assert s1.toppings == []
        assert s1.topping_prices == {'S': 1.75, 'M': 2.50, 'L': 3.00}
        s2 = CustomSalad('M')
        assert s2.get_size() == 'M'
        assert s2.get_price() == 10.75
        s3 = CustomSalad('S')
        assert s3.get_size() == 'S'
        assert s3.get_price() == 8.75

    def test_add_topping(self):
        s1 = CustomSalad('M') 
        s1.add_topping('tomato')
        assert 'tomato' in s1.toppings 
        assert s1.price == 13.25

    def test_get_salad_details(self):
        s1 = CustomSalad('M')
        s1.add_topping('tomato')
        expected_string = 'CUSTOM SALAD\nSize: M\nToppings:\n\t+ tomato\nPrice: $13.25\n'
        assert s1.get_salad_details() == expected_string
    

class Test_SpecialtySalad:

    def test_init(self):
        s1 = SpecialtySalad('L', 'Fruit')
        assert s1.get_price() == 16.50
        assert s1.get_size() == 'L'
        assert s1.get_salad_details() == 'SPECIALTY SALAD\nSize: L\nName: Fruit\nPrice: $16.50\n'
        s2 = SpecialtySalad('M', 'Caesar')
        assert s2.get_size() == 'M'
        assert s2.get_price() == 14.50
        s3 = SpecialtySalad('S', 'Greek')
        assert s3.get_size() == 'S'
        assert s3.get_price() == 12.50


    def test_get_salad_details(self):
        s1 = SpecialtySalad('L', 'Caesar')
        assert s1.get_salad_details() == 'SPECIALTY SALAD\nSize: L\nName: Caesar\nPrice: $16.50\n'

class Test_SaladOrder:

    def test_init(self):
        s1 = SaladOrder(123000)
        assert s1.get_time() == 123000
        assert s1.salads == []

    def test_set_time(self):
        s1 = SaladOrder(113000)
        s1.set_time(123000)
        assert s1.get_time() == 123000

    def test_get_time(self):
        s1 = SaladOrder(113000)
        s1.set_time(123000)
        assert s1.get_time() == 123000

    def test_add_salad(self):
        order = SaladOrder(113000)
        s1 = CustomSalad('S') 
        order.add_salad(s1)
        assert s1 in order.salads

    def test_info(self):
        order = SaladOrder(123000)
        s1 = CustomSalad('M')
        s1.add_topping('tomato')
        s2 = SpecialtySalad('L', 'Fruit')
        order.add_salad(s1)
        order.add_salad(s2)    
        expected_string = ('***\n'
                     'Order Time: 123000\n'
                     f'{s1.get_salad_details()}\n'
                     '----\n'
                     f'{s2.get_salad_details()}\n'
                     '----\n'
                     'TOTAL ORDER PRICE: $29.75\n'
                     '***\n')
        assert order.info() == expected_string

class Test_OrderQueue:

    def test_init(self):
        q1 = OrderQueue.OrderQueue()
        assert q1.is_empty() == True
        assert q1.size() == 0

    def test_move_up(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(123000) 
        o2 = SaladOrder(103000) 
        q1.add_order(o1)
        q1.add_order(o2)
        q1.move_up(q1.size())
    
    def test_move_down(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(103000) 
        o2 = SaladOrder(123000)
        o3 = SaladOrder(124000) 
        q1.add_order(o1)
        q1.add_order(o2)
        q1.add_order(o3)
        q1.move_down(1)
        p1 = q1.process_next_order()
        p2 = q1.process_next_order()
        assert '103000' in p1
        assert '123000' in p2

    def test_add_order(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(123000)
        q1.add_order(o1)
        assert q1.size() == 1

    def test_process_next_order(self):
        q1 = OrderQueue.OrderQueue()
        assert q1.process_next_order() == ''
        o1 = SaladOrder(123000)
        q1.add_order(o1)
        assert q1.process_next_order() == o1.info()
        assert q1.is_empty() == True

    def test_min_child(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(123000)  
        o2 = SaladOrder(125000) 
        o3 = SaladOrder(103000)  
        q1.add_order(o1)
        q1.add_order(o2)
        q1.add_order(o3)
        assert q1.min_child(1) == 3 
        o4 = SaladOrder(101000) 
        q1.add_order(o4)
        assert q1.min_child(2) == 4 

    def test_del_min(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(123456)
        q1.add_order(o1)
        q1.del_min()
        assert q1.is_empty() == True

    def test_is_empty(self):
        q1 = OrderQueue.OrderQueue()
        o1 = SaladOrder(123000)
        o2 = SaladOrder(103000)
        q1.add_order(o1)
        q1.add_order(o2)
        assert q1.del_min() == o2 
        assert q1.size() == 1

    def test_size(self):
        q1 = OrderQueue.OrderQueue()
        assert q1.size() == 0
        o1 = SaladOrder(123000)
        q1.add_order(o1)
        assert q1.size() == 1
