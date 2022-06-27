from pyparsing import null_debug_action


class Node:
        def __init__(self, val, next = None):
            self.val = val
            self.next = next

class Stack:
            
    def __init__(self):
        self.stack_size = 0
        self.top_node = None
        self.stack_min = None
    
    def push(self, val):
        new = Node(val)
        new.next = self.top_node
        self.top_node = new
        self.stack_size += 1

        if not self.stack_min:
            self.stack_min = Node(val)
        else:
            if val < self.stack_min.val:
                new_min = Node(val)
                new_min.next = self.stack_min
                self.stack_min = new_min

    def pop(self):
        if self.isEmpty():
            print('No element to return, stack is empty')
            return None
        popped = self.top_node
        self.top_node = popped.next
        popped.next = None
        self.stack_size -= 1

        if popped.val == self.stack_min.val:
            self.stack_min = self.stack_min.next

        return popped.val

    def top(self):
        if self.isEmpty():
            print('No element to return, stack is empty')
            return None
        return self.top_node.val

    def isEmpty(self):
        return self.stack_size == 0

    def size(self):
        return self.stack_size
    
    def min(self):
        if self.isEmpty():
            print('No element to return, stack is empty')
            return None
        return self.stack_min.val

print('\n')

# sample execution trace
myStack = Stack()
myStack.push(42)
print('Top of stack1: ', myStack.top())
print('Size of stack1: ', myStack.size())
popped_value = myStack.pop()
print('Popped value: ', popped_value)
print('Size of stack1: ', myStack.size())
print('\n')

# pop off more items than you push
popped_value2 = myStack.pop()
print('\n')

# test min()
for num in [42, 45, 1, -1, 5]:
    myStack.push(num)
    print('Minimum element in stack1 is: ', myStack.min())

for i in range(5):
    dummy = myStack.pop()
    print('Minimum element in stack1 is: ', myStack.min())
print('\n')

# handle string objects
myStack2 = Stack()
for string in ['b', 'abcd','ABCD', 'A','a']:
    myStack2.push(string)
    print('Top of stack2: ', myStack2.top())
    print('Size of stack2: ', myStack2.size())
    print('Minimum element in stack2 is: ', myStack2.min())
for i in range(5):
    popped_value = myStack2.pop()
    print('Popped value: ', popped_value)
    print('Minimum element in stack2 is: ', myStack2.min())
print('\n')


class Queue:
    def __init__(self):
        self.queue_front = None
        self.queue_rear = None
        self.queue_size = 0

    def enqueue(self, elem):
        new = Node(elem)
        if self.isEmpty():
            self.queue_front = new
            self.queue_rear = new
        else:
            self.queue_rear.next = new
            self.queue_rear = new
        self.queue_size += 1

    def dequeue(self): # what if there's only one node
        if self.isEmpty():
            print('No element to return, queue is empty')
            return None
        else:
            popped = self.queue_front
            self.queue_front = popped.next
            if self.queue_size == 1:
                self.queue_rear = None
            popped.next = None
            self.queue_size -= 1
            return popped.val

    def rear(self):
        return self.queue_rear.val

    def front(self):
        return self.queue_front.val
    
    def size(self):
        return self.queue_size
    
    def isEmpty(self):
        return self.queue_size == 0

# sample execution trace
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print('Size of queue1: ', myQueue.size())
print('Front of queue1: ', myQueue.front())
print('Rear of queue1: ', myQueue.rear())
dequeuedItem = myQueue.dequeue()
print('Dequeued item: ', dequeuedItem)
print('\n')

# dequeue more items than you enqueue
dequeuedItem = myQueue.dequeue()
dequeuedItem = myQueue.dequeue()
dequeuedItem = myQueue.dequeue()
print('\n')

# handle string objects
myQueue2 = Queue()
myQueue2.enqueue('one')
myQueue2.enqueue('two')
myQueue2.enqueue('three')
print('Size of queue2: ', myQueue2.size())
print('Front of queue2: ', myQueue2.front())
print('Rear of queue2: ', myQueue2.rear())
dequeuedItem = myQueue2.dequeue()
print('Dequeued item: ', dequeuedItem)
print('\n')