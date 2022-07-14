class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.max = len(self.iterable)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.max:
            self.i += 1
            return self.iterable[self.i - 1]
        else:
            self.i = 1
            return self.iterable[0]


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator([2, 'hello', 4, 6, 8, 10])
    for i in cyclic_iterator:
        print(i)
