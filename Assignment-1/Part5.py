from Part4 import Node, LinkedList
from Part3 import Stack

def reverseLinkedList_iter(llist):

    result = LinkedList()

    if llist.size() == 0:
        return result
    
    current = llist.getFirst()
    result.last = Node(current.data)
    result.first = result.last
    result.list_size += 1

    while current.next:
        current = current.next
        new = Node(current.data, result.first)
        result.first = new
        result.list_size += 1
    return result

llist = LinkedList()

for i in range(10):
    node = Node(i)
    llist.push(node)

llist.printList()
reverseLinkedList_iter(llist).printList()
llist.printList()

def reverseLinkedList_stack(llist):

    result = LinkedList()
    stack = Stack()

    if llist.size() == 0:
        return result

    current = llist.getFirst()
    while current:
        stack.push(current.data)
        current = current.next
    while stack.size() > 0:
        result.push(Node(stack.pop()))

    return result

reverseLinkedList_stack(llist).printList()
llist.printList()


def reverseLinkedList_rec(llist):

    def helper(head):
        if not head.next:
            return head
        rest = helper(head.next)
        head.next.next = head
        head.next = None
        return rest

    result = LinkedList()
    current = llist.getFirst()
    while current:
        result.push(Node(current.data))
        current = current.next


    helper(result.first)
    result.last, result.first = result.first, result.last
    
    return result

reverseLinkedList_rec(llist).printList()
llist.printList()