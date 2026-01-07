# Implementation of the queue ADT using a circular array
from array import Array   # <-- your custom Array

class CircularQueue:
    # Creates an empty Queue
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._qArray)

    def __len__(self):
        return self._count

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        self._back = (self._back + 1) % len(self._qArray)
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[self._front]
        self._front = (self._front + 1) % len(self._qArray)
        self._count -= 1
        return item

if __name__ == "__main__":
    Q = CircularQueue(8)

    Q.enqueue(28)
    Q.enqueue(19)
    Q.enqueue(45)
    Q.enqueue(13)
    Q.enqueue(7)

    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())

    Q.enqueue(55)
    print(Q.dequeue())
