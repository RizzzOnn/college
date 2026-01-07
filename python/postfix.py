class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1

    # Add item to stack
    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    # Remove item from stack
    def pop(self):
        value = self.stack[self.top]
        self.top -= 1
        return value


# Function to evaluate postfix expression
def evaluate_postfix(expression):
    stack = Stack(len(expression.split()))

    for item in expression.split():

        # If item is a number, push into stack
        if item.isdigit():
            stack.push(int(item))

        # If item is an operator
        else:
            b = stack.pop()
            a = stack.pop()

            if item == '+':
                stack.push(a + b)
            elif item == '-':
                stack.push(a - b)
            elif item == '*':
                stack.push(a * b)
            elif item == '/':
                stack.push(a / b)

    # Final result
    return stack.pop()


# Main program
postfix = input("Enter postfix expression: ")
result = evaluate_postfix(postfix)
print("Result:", result)
