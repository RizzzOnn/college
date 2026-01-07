#Queue implementation for managing customer service requests at Bhatbhateni Supermarket


import time
from queue import Queue

if __name__ == "__main__":
    customer_queue = Queue()

    customer_queue.enqueue(("Customer 1 - Return Item", 4))
    customer_queue.enqueue(("Customer 2 - Billing Issue", 7))
    customer_queue.enqueue(("Customer 3 - Membership Inquiry", 3))
    customer_queue.enqueue(("Customer 4 - Exchange Product", 8))
    customer_queue.enqueue(("Customer 5 - Payment Problem", 5))


    while not customer_queue.isEmpty():
        customer, service_time = customer_queue.dequeue()
        print(f"Serving: {customer}")
        print(f"Taken time: {service_time} seconds...")
        time.sleep(service_time)
        print(f"Finished serving: {customer}\n")
