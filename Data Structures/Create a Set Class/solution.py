class Set:
    def __init__(self, set):
        self.start = 0
        self.set = []
        [self.set.append(x) for x in set if x not in self.set]

    def add(self, element):
        if element in self.set:
            print('The element is already present')
        else:
            self.set.append(element)

    def remove(self, element):
        if element in self.set:
            self.set.remove(element)
        else:
            print('The element does not exist.')

    def size(self):
        print(len(self.set))

    def show(self):
        print(self.set)

    def has(self, element):
        print(element in self.set)

    # below are set functions
    def union(self, another_set):
        union = []
        [union.append(x) for x in self.set]
        [union.append(x) for x in list(another_set) if x not in union]
        return union

    def intersection(self, another_set):
        intersect = []
        [intersect.append(x) for x in self.set if x in another_set]
        return intersect

    def difference(self, another_set):
        difference = []
        [difference.append(x) for x in self.set if x not in another_set]
        return difference

    def is_subset_of(self, another_set):
        for x in self.set:
            if x not in another_set:
                return False
        return True

    # iteration purpose
    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.set):
            raise StopIteration
        else:
            self.start += 1
            return self.set[self.start - 1]


# below are some 'Set' class implementations
A = Set([1, 2, 3, 3, 1, 'Taco', 'Cat', 'Awesome'])
A.show()
B = Set([1, 2, 3, 4, 5])
B.remove(2)
B.remove(5)
B.show()
C = Set([4, 3, 6])
C.has(5), C.size()
D = Set([1, 2, 3, 4, 5, 6, 7])
D_list = []
[D_list.append(x) for x in D]
print(D_list, type(D_list))
