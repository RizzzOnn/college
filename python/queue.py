#Implementation of the queue ADT using python list
class Queue:
    #Creates an empty Queue
    def __init__(self):
        self._qList = list()

    # Returs True If the queue is empty
    def isEmpty (self) :
        return len(self) == 0

    # Returns the number of items in the queue
    def __len__(self):
        return len(self._qList)
    # Adds the given item to the queue
    def enqueue (self, item):
        self._qList.append(item)
    # Remives and returns the first item in the queue
    def dequeue (self):
        assert not self.isEmpty(), "Cannot dequeue from an epmty queue."
        return self._qList.pop(0)


#Example usage
if __name__ == "__main__":
    Q = Queue()
    Q.enqueue(28)
    Q.enqueue(19)
    Q.enqueue(45)
    Q.enqueue(13)
    Q.enqueue(7)

    print(Q.dequeue())
    print(Q.dequeue())
