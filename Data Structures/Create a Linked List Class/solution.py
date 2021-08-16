class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def size(self):
        return self.length

    def head(self):
        return self.head

    def add(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            current_node = self.head
            while current_node:
                prev = current_node
                current_node = current_node.next
            current_node = Node(element)
            prev.next = current_node
        self.length += 1

    def add_at(self, index, element):
        if index < 0 or index >= self.length:
            print('Error: Invalid Index')
        elif index == 0:
            prev = self.head
            self.head = Node(element)
            self.head.next = prev
        else:
            current_node = self.head
            for i in range(index):
                prev = current_node
                current_node = current_node.next
            pointer = Node(element)
            prev.next = pointer
            pointer.next = current_node

    def remove(self, element):  # assumes 'element' must be in the Linked List
        if self.head is None:
            print('The linked list is empty')
        else:
            current_node = self.head
            # if the head is the element to be removed
            if current_node.element == element:
                self.head = current_node.next
            else:
                while current_node:
                    if current_node.element == element:
                        break
                    prev = current_node
                    current_node = current_node.next

                prev.next = current_node.next
                current_node = None
            self.length -= 1

    def remove_at(self, index):
        current_node = self.head
        if index == 0:
            print(f'{self.head.element} is removed.')
            self.head = current_node.next
            self.length -= 1
        elif index < 0 or index >= self.length:
            print('Error: Invalid Index')
        else:
            for i in range(index):
                current_node = current_node.next
                prev = current_node
            print(f'{current_node.element} is removed.')
            prev.next = current_node.next
            current_node = None
            self.length -= 1

    def is_empty(self):
        if self.length:
            return True
        return False

    def index_of(self, element):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.element == element:
                return f'Index of {element}: {index}'
            current_node = current_node.next
            index += 1
        return -1

    def element_at(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return f'Element at index {index}: {current_node.element}'

    def show(self):
        current_node = self.head
        print('Below are the elements of linked list:\n----------')
        while current_node:
            print(current_node.element)
            current_node = current_node.next
        print('----------')


linked_list = LinkedList()
linked_list.add('Mon')
linked_list.add('Tue')
linked_list.add('Wed')
linked_list.add('Thu')
linked_list.remove('Thu')
linked_list.add_at(0, 'Holidayy')
print(linked_list.index_of('Tue'))
print(linked_list.element_at(2))
linked_list.remove_at(3)
linked_list.show()
