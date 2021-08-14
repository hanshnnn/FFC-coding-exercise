class CircularQueue:
    def __init__(self, length):
        self.queue = [None for x in range(length)]
        self.read = 0
        self.write = 0
        self.length = length
        self.max = length - 1

    def enqueue(self, add):
        if self.write > self.max:
            self.queue[self.write - self.length * (self.write // self.length)] = add
            print(add)
        else:
            self.queue[self.write] = add
        self.write += 1

    def dequeue(self):
        if self.read > self.write:
            print('Sorry, you should not dequeue past the write pointer.')
            return None
        elif self.read < self.max:
            print(self.queue[self.read])
            self.queue[self.read] = None
            self.read += 1
        else:
            print(self.queue[self.read - self.length * (self.read // self.length)])
            self.queue[self.read - self.length * (self.read // self.length)] = None
            self.read += 1

    def show(self):
        print(self.queue)
