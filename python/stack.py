class Stack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def push(self, item):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push.")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def length(self):
        return self.top + 1


if __name__ == "__main__":
    s = Stack(3)

    s.push(10)
    s.push(20)
    s.push(30)

    s.push(40)  # overflow

    print("Top element:", s.peek())

    s.pop()
    print("Stack size:", s.length())

    s.pop()
    s.pop()
    s.pop()  # underflow