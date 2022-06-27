from csv import reader
from telnetlib import WILL
import time

from numpy import insert

class ListPhoneBook:
    def __init__(self) -> None:
        self.entries = []
    
    def size(self):
        return len(self.entries)

    def insert(self, name, phoneNumber):
        self.entries.append({'name': name, 'phoneNumber': phoneNumber})

    def find(self, name):
        for entry in self.entries:
            if entry['name'] == name:
                return entry['phoneNumber']
        return -1

print('\nEx5:')
print('\nListPhoneBook:')
listPhoneBook = ListPhoneBook()
listPhoneBook.insert('ABC', 1111111111)
listPhoneBook.insert('XYZ', 9999999999)
listPhoneBook.insert('DEF', 2222222222)
print(listPhoneBook.size())
print(listPhoneBook.find('ABC'))
print(listPhoneBook.find('XYZ'))
print(listPhoneBook.find('PQR'))

class Node:
    def __init__(self, name=None, phoneNumber=None, left=None, right=None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.left = left
        self.right = right

class BinarySearchTreePhoneBook:

    def __init__(self):
        self.root = None
        self.bookSize = 0
    
    def size(self):
        return self.bookSize

    def insert(self, name, phoneNumber):
        self.bookSize += 1
        if not self.root:
            self.root = Node(name, phoneNumber)
            return
        current = self.root
        while current:
            if name <= current.name:
                if not current.left:
                    current.left = Node(name, phoneNumber)
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(name, phoneNumber)
                    break
                else:
                    current = current.right      

    def find(self, name):
        def findHelper(root, name):
            if not root: return -1
            if name == root.name: 
                return root.phoneNumber
            else:
                if name < root.name:
                    return findHelper(root.left, name)
                else:
                    return findHelper(root.right, name)

        return findHelper(self.root, name)

print('\nBSTPhoneBook:')
bstPhoneBook = BinarySearchTreePhoneBook()
bstPhoneBook.insert('ABC', 1111111111)
bstPhoneBook.insert('XYZ', 9999999999)
bstPhoneBook.insert('DEF', 2222222222)
print(bstPhoneBook.size())
print(bstPhoneBook.find('ABC'))
print(bstPhoneBook.find('XYZ'))
print(bstPhoneBook.find('PQR'))

print('\nEx6:')
print('\nListPhoneBook:')

listPhoneBook = ListPhoneBook()

with open('data.csv', 'r') as data:
    phoneBook = reader(data)
    t0 = time.time()
    for line in phoneBook:
        listPhoneBook.insert(line[0], line[1])
    t1 = time.time()
    print('Insert time: ', t1 - t0)
    print('Book size: ', listPhoneBook.size())

with open('search.txt', 'r') as data:
    names = data.read().splitlines()
    findCalled = 0
    t0 = time.time()
    for name in names:
        result = listPhoneBook.find(name)
        if result == -1:
            exit('Failed to find a name in phone book.')
        findCalled += 1
    print('Called find()', findCalled, 'times')
    t1 = time.time()
    print('Search took: ', t1 - t0)

print('\nBSTPhoneBook:')
bstPhoneBook = BinarySearchTreePhoneBook()

with open('data.csv', 'r') as data:
    phoneBook = reader(data)
    t0 = time.time()
    for line in phoneBook:
        bstPhoneBook.insert(line[0], line[1])
    t1 = time.time()
    print('Insert time: ', t1 - t0)
    print('Book size: ', bstPhoneBook.size())

with open('search.txt', 'r') as data:
    names = data.read().splitlines()
    findCalled = 0
    t0 = time.time()
    for name in names:
        result = bstPhoneBook.find(name)
        if result == -1:
            exit('Failed to find a name in phone book.')
        findCalled += 1
    print('Called find()', findCalled, 'times')
    t1 = time.time()
    print('Search took: ', t1 - t0)

# Output:

# ListPhoneBook:
# Insert time:  1.0352158546447754 seconds
# Book size:  1000000
# Called find() 1000 times
# Search took:  29.063350200653076 seconds

# BSTPhoneBook:
# Insert time:  9.109257936477661 seconds
# Book size:  1000000
# Called find() 1000 times
# Search took:  0.009068012237548828 seconds

# Why is there a difference?

# The insert() method in ListPhoneBook appends the new entry to the end of the list,
# which takes O(1) time. To perform insert() in BSTPhoneBook=, we will
# have to find the correct location, which takes O(log(n)) time. Therefore, insert() is 
# faster in ListPhoneBook than in BSTPhoneBook.

# To search in ListPhoneBook, since it is unordered, we will have to perform a linear search,
# which takes O(n) time. The ordered BSTPhoneBook on the other hand, only takes O(log(n)) time 
# for searching. Therefore, insert() is faster in BSTPhoneBook than in ListPhoneBook.