# This is prime numbers iterator starting iteration from a given number
from itertools import count

class PrimesIterator:

    def __init__(self, start=2):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        for i in count(self.start):
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                self.start = i + 1
                return i


for n in PrimesIterator(1_000_000): print(n)


