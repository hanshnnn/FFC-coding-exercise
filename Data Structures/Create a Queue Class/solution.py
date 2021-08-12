class Queue:
    def __init__(self, queue):
        self.queue = queue

    def enqueue(self, element):
        self.queue.append(element)

    def is_empty(self):
        if not self.queue:
            return 'The queue is empty.'
        else:
            return 'The queue is not empty.'

    def dequeue(self):
        if self.is_empty() == 'The queue is not empty.':
            last_element = self.queue[0]
            self.queue.pop(0)
            return last_element
        else:
            print('The queue is empty.')

    def front(self):
        if self.is_empty() == 'The queue is not empty.':
            return self.queue[0]
        else:
            print('The queue is empty.')

    def size(self):
        return len(self.queue)
