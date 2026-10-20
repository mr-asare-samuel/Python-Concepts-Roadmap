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

    def get_head(self):
        if self.head is None:
            return None
        return self.head.data

    def get_tail(self):
        current = self.head

        while current is not None:
            if current.next is None:
                return current.data
            current = current.next

        return None

    # def get_tail(self):
    #     if self.head is None:
    #         return None

    #     current = self.head

    #     while current.next is not None:
    #         current = current.next

    #     return current.data


    def get_value(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return current.data
            current = current.next

        return None

    def get_at_index(self, index):
        current = self.head
        position = 0

        while current is not None:
            if position == index:
                return current.data
            current = current.next
            position += 1

        return None
            
            





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
print(ll.get_tail())   
print(ll.get_value(12))   




# Traversal Cost (O(n))
"""
Traversal methods (get_value, get_tail, get_at_index) are O(n) because they
walk node by node from the head following next pointers.
An index parameter does not change this: unlike an array, which jumps
directly to an index in O(1), a linked list has no random access.
For huge datasets this can mean visiting every node.
When fast random access is needed, use an array, or a hybrid such as a
skip list that adds extra forward pointers to jump further per step.
"""

# Exporting / Importing the Instance
"""
You can export the LinkedList instance from the file where it is created
(for example a module-level variable such as `ll` at the bottom of this file).
Another file can import it with a from-import, e.g. `from dsa.linked_list import ll`.
If that other file also runs this module's initialization (creating `ll` again,
or constructing its own LinkedList), you get a second, separate list.
To share one instance, create it in one place and either pass it around or
keep it in a module-level variable that other files import without rebuilding it.
"""
