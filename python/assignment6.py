class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_before(self, target, data):
        if self.head is None:
            print("List is empty")
            return

        # If target is at head
        if self.head.data == target:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        curr = self.head

        while curr and curr.data != target:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Element not found")
        else:
            new_node = Node(data)
            prev.next = new_node
            new_node.next = curr

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Main program
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.display()

ll.insert_before(30, 25)
ll.display()
# Inserting before head