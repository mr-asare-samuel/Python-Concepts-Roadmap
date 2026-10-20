class Node:
    """
    A single node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next (Node | None): Reference to the next node in the list,
            or None if this is the last node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list.

    Maintains a reference to the head node and supports inserting
    at the front or back, removing by value, and listing all values.

    Attributes:
        head (Node | None): The first node in the list, or None if
            the list is empty.
    """
    def __init__(self):
        self.head = None

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node


    def remove(self, data):
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return

            previous = current
            current = current.next



    def ll_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items




ll = LinkedList()
ll.add_first(34)
ll.add_first(20)
ll.add_first(10)
ll.add_last(100)
ll.add_last(10)
ll.add_last(20)
ll.add_first(5)
ll.remove(20)

print(ll.ll_list())

ll.remove(10)

print(ll.ll_list())
print(type(ll))
        