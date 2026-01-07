from queue import Queue
import time

if __name__ == "__main__":
    print_queue = Queue()
    print_queue.enqueue("Document.pdf")
    print_queue.enqueue("Image2.png")
    print_queue.enqueue("Report3.docx")
    print_queue.enqueue("Presentation4.pptx")


    while not print_queue.isEmpty():
        current_job = print_queue.dequeue()
        print(f"Printing: {current_job}....")
        time.sleep(4) # Simulating the time taken to print the document
        print(f"Finished Printing: {current_job}...\n")