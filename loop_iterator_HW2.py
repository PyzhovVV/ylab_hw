from dataclasses import dataclass


@dataclass
class CyclicIterator:
    iterable: set | list | tuple | dict | frozenset | str | range

    def __iter__(self):
        self.max: int = len(self.iterable)
        self.i: int = 0
        return self

    def __next__(self):
        if self.i < self.max:
            self.i += 1
            return self.iterable[self.i - 1]
        else:
            self.i = 1
            return self.iterable[0]


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator('tuple([1, 3, 5, 4, 3, 6, 8])')
    for i in cyclic_iterator:
        print(i)
