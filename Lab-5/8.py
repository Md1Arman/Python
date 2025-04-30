# 8.	Write a menu-driven program to implement the Queue data structure.


class Queue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.is_empty():
            print(f"Removed element: {self.queue.pop(0)}")
        else:
            print("Queue is empty. Nothing to remove.")

    def peek(self):
        if not self.is_empty():
            print(f"Front element: {self.queue[0]}")
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if not self.is_empty():
            print("Queue contents (front to rear):", self.queue)
        else:
            print("Queue is empty.")

def queue_menu():
    queue = Queue()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Remove)")
        print("3. Peek (Front Element)")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter element to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

queue_menu()
