class PriorityQueue:
    def __init__(self, queue):
        if input('Is your priority Queue ordered?(Y/N)\n') == 'N':
            print('Okay then, we will arrange it for you;)')
            temp = [x[1] for x in queue]
            temp.sort()
            sorted_queue = []
            for value in temp:
                for element in queue:
                    if element[1] == value:
                        sorted_queue.append(element)
                        break
            self.queue = sorted_queue
        else:
            self.queue = queue

    # auto arrange sequence by priority
    def enqueue(self, element):
        self.queue.append(element)
        i = -1
        while i != -len(self.queue) and self.queue[i][1] < self.queue[i-1][1]:
            self.queue[i-1], self.queue[i] = self.queue[i], self.queue[i-1]
            i -= 1

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

