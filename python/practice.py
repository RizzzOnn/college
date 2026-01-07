from stack import Stack
from queue import Queue

def reverse_individual_words(s: str) -> str:
    words = s.split()
    result = ""
    for word in words:
        result += word[::-1] + " "
    return result.strip()

def compare_stack_queue_orders(stack_values: list, queue_values: list) -> bool:
    # Initialize Stack with capacity equal to number of elements
    s = Stack(len(stack_values))
    for val in stack_values:
        s.push(val)
        
    # Initialize Queue
    q = Queue()
    for val in queue_values:
        q.enqueue(val)
        
    stack_output = []
    while not s.is_empty():
        stack_output.append(s.pop())
        
    queue_output = []
    while not q.isEmpty():
        queue_output.append(q.dequeue())
        
    return stack_output == queue_output

if __name__ == "__main__":
    # Problem 1: Reverse individual words
    input_str = "Hello World"
    print(f"Input: {input_str}")
    print(f"Output: {reverse_individual_words(input_str)}")
    
    # Problem 2: Compare Stack and Queue
    # Case 1: Identical removal order
    stack_in = [1, 2, 3] # Stack pops: 3, 2, 1
    queue_in = [3, 2, 1] # Queue dequeues: 3, 2, 1
    print(f"\nComparing Stack inputs {stack_in} and Queue inputs {queue_in}")
    result = compare_stack_queue_orders(stack_in, queue_in)
    print(f"Same removal order? {result}")

    # Case 2: Different removal order
    stack_in2 = [1, 2, 3] # Stack pops: 3, 2, 1
    queue_in2 = [1, 2, 3] # Queue dequeues: 1, 2, 3
    print(f"\nComparing Stack inputs {stack_in2} and Queue inputs {queue_in2}")
    result2 = compare_stack_queue_orders(stack_in2, queue_in2)
    print(f"Same removal order? {result2}")
