import random
import math

sorted_arr = []
input_arr = [random.randint(1, 1000) for i in range(1000)]

def quick_sort():
    return

def merge_k():
    return

class HeapNode:
    def __init__(self, val, i, arr_i):
        self.val = val
        self.i = i
        self.arr_i = arr_i

class MinHeap:

    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def pop(self):
        popped = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        self.heapify_down()
        return popped

    def heapify_up(self):
        index = self.size - 1
        parent_index = (index - 1) // 2
        while parent_index > -1 and self.items[index].val < self.items[parent_index].val:
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self):
        index = 0
        smaller_child_index = left_child_index = index * 2 + 1
        while left_child_index < self.size:
            right_child_index = index * 2 + 2
            if right_child_index < self.size and self.items[left_child_index].val > self.items[right_child_index].val:
                smaller_child_index = right_child_index
            if self.items[index].val > self.items[smaller_child_index].val:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
                index = smaller_child_index
                smaller_child_index = left_child_index = index * 2 + 1
            else: 
                break

def external_sort():
    
    i = 0
    ram_cap = 100
    ram = []
    num_partition = math.ceil(len(input_arr)/ram_cap)
    #first sort the input arr 100 entries at a time
    while i < len(input_arr):
        if i + ram_cap >= len(input_arr):
            input_arr[i:] = sorted(input_arr[i:])
        else:
            input_arr[i:i+ram_cap] = sorted(input_arr[i:i+ram_cap])
        i += ram_cap

    min_heap = MinHeap()
    for i in range(num_partition):
        index = i * ram_cap
        node = HeapNode(input_arr[index], index, i)
        min_heap.push(node)
        
    i = 0
    while i < len(input_arr):
        popped = min_heap.pop()
        if popped.i < len(input_arr) - 1 and popped.i + 1 < popped.arr_i * ram_cap + ram_cap:
            node = HeapNode(input_arr[popped.i + 1], popped.i + 1, popped.arr_i)
            min_heap.push(node)
        ram.append(popped.val)
        if len(ram) == ram_cap:
            sorted_arr.extend(ram)
            ram = []
        i+=1

sorted_arr_correct = sorted(input_arr)
external_sort()
print(sorted_arr)
print(sorted_arr == sorted_arr_correct)



    

