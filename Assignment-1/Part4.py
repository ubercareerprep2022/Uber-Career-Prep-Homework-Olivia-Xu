from subprocess import list2cmdline


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.list_size = 0

    def push(self, node):
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.list_size += 1
    
    def pop(self):
        if self.list_size == 0:
            print('No element to return, list is empty')
            return None
        popped = self.last
        self.remove(self.list_size - 1)
        return popped

    def insert(self, index, node):
        if index > self.list_size - 1 or index < 0: return
        if index == 0:
            node.next = self.first
            self.first = node
            self.list_size += 1
            return

        prev = None
        current = self.first
        current_index = 0
        while current_index < index:
            prev = current
            current = current.next
            current_index += 1
        prev.next = node
        node.next = current
        self.list_size += 1

    def remove(self, index):
        if index > self.list_size - 1 or index < 0: return
        if index == 0:
            self.first = self.first.next
            self.list_size -= 1
            return

        prev = None
        current = self.first
        current_index = 0
        while current_index < index:
            prev = current
            current = current.next
            current_index += 1
        prev.next = current.next
        self.list_size -= 1
    
    def elementAt(self, index):
        if index > self.list_size - 1 or index < 0: return None
        current = self.first
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1
        return current

    def size(self):
        return self.list_size

    def printList(self):
        string = ''
        current = self.first
        for i in range(self.list_size):
            string += str(current.data) + " "
            current = current.next
        print('List elements: ', string)
    
    def getFirst(self):
        return self.first

    def hasCycle(self):
        if self.list_size == 0: return False
        pointer1 = self.first
        pointer2 = self.first.next
        while pointer1 != pointer2 and pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        if pointer1 == pointer2:
            return True
        if not pointer2 or not pointer2.next:
            return False

    def isPalindrome(self):
        if self.list_size == 0 or self.list_size == 1: return True
        pointer1 = self.first
        pointer2 = self.first.next
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        pointer2 = pointer1
        pointer1 = self.first
        str1 = ''
        str2 = ''
        while pointer2:
            str1 += str(pointer1.data)
            str2 += str(pointer2.data)
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return str1 == str2[::-1]

print("\ntestPushBackAddsOneNode")
node1 = Node(1)
llist = LinkedList()
llist.push(node1)
print('Size of the list: ', llist.size())
llist.printList()

print('\ntestPopBackRemovesCorrectNode')
print('Popped value: ', llist.pop().data)
print('Size of the list: ', llist.size())
llist.printList()

for i in range(5):
    node = Node(i)
    llist.push(node)

print('\ntestEraseRemovesCorrectNode')
llist.printList()
llist.remove(3)
llist.printList()
llist.remove(0)
llist.printList()

print('\ntestEraseDoesNothingIfNoNode')
llist.remove(100)
llist.printList()

print('\ntestElementAtReturnNode')
print("Element at index 1: ", llist.elementAt(1).data)

print('\ntestElementAtReturnsNoNodeIfIndexDoesNotExist')
print("Element at index 100: ", llist.elementAt(100))

print('\ntestInsertAddsCorrectNode')
llist.insert(2, Node(-1))
llist.printList()

print('\ntestInsertDoesNothingIfIndexDoesNotExist')
llist.insert(100, Node(-1))
llist.printList()

print('\ntestSizeReturnsCorrectSize')
llist.printList()
print("List size: ", llist.size())

print('\ntestHasCycle')
llist.printList()
print("List has cycle: ", llist.hasCycle())
llist.push(llist.getFirst())
llist.printList()
print("List has cycle: ", llist.hasCycle())

print('\ntestIsPalindrome')
llist = LinkedList()
llist.printList()
print('List is a palindrome: ', llist.isPalindrome())
llist.push(Node(1))
llist.printList()
print('List is a palindrome: ', llist.isPalindrome())
for i in [2,3,2]:
    llist.push(Node(i))
llist.printList()
print('List is a palindrome: ', llist.isPalindrome())
llist.push(Node(1))
llist.printList()
print('List is a palindrome: ', llist.isPalindrome())
llist.insert(3, Node(3))
llist.printList()
print('List is a palindrome: ', llist.isPalindrome())