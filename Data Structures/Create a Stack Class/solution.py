class Stack:
    def __init__(self, stack):
        self.stack = stack

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        if not self.stack:
            return 'The stack is empty.'
        else:
            return 'The stack is not empty.'

    def pop(self):
        if self.is_empty() == 'The stack is not empty.':
            last_element = self.stack[-1]
            self.stack.pop()
            return last_element
        else:
            print('The stack is empty.')

    def peek(self):
        if self.is_empty() == 'The stack is not empty.':
            print(self.stack[-1])
        else:
            print('The stack is empty.')

    def clear(self):
        self.stack = []


x = Stack(['a'])
x.pop()
print(x.is_empty())
