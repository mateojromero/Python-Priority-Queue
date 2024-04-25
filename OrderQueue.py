
from SaladOrder import SaladOrder

class OrderQueue:
    def __init__(self):
        self.heap_list = [None]
        self.current_size = 0

    def move_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i].get_time() < self.heap_list[i // 2].get_time():
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
    
    def move_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i].get_time() > self.heap_list[mc].get_time():
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def add_order(self, order):
        self.heap_list.append(order)
        self.current_size += 1
        self.move_up(self.current_size)

    def process_next_order(self):
        if self.current_size == 0:
            return '' 
        next_order = self.heap_list[1] 
        self.heap_list[1] = self.heap_list[self.current_size] 
        self.current_size -= 1  
        self.heap_list.pop()  
        self.move_down(1)  
        return next_order.info()

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2].get_time() < self.heap_list[i * 2 + 1].get_time():
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.move_down(1)
        return val

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size
