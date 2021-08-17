class Node:
    def __init__(self, element, prev):
        self.element = element
        self.prev = prev
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        if self.head is None:
            self.head = Node(element, None)
            self.tail = self.head
        else:
            self.tail.next = Node(element, self.tail)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def remove(self, element):
        if self.head is None:
            print('The list is empty.')
        elif self.head.element == element:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.element == element:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            while current_node:
                if current_node.element == element:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    current_node = None
                    break
                current_node = current_node.next

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        current_node = self.head
        while current_node:
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = current_node.next

    def show(self):
        current_node = self.head
        print('Below are the elements of linked list:\n----------')
        while current_node:
            print(current_node.element)
            current_node = current_node.next
        print('----------')


dlinked_list = DoublyLinkedList()
dlinked_list.add('Mon')
dlinked_list.add('Tue')
dlinked_list.add('Wed')
dlinked_list.add('Thu')
dlinked_list.add('Fri')
dlinked_list.remove('Wed')
dlinked_list.reverse()
dlinked_list.show()
