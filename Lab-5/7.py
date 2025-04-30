# 7.	Write a menu-driven program to implement the stack data structure.
# Stack implementation using a list

class Stack:
    def __init__(self):
        self.stack = []  

    # Push 
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed onto stack.")

    # Pop 
    def pop(self):
        if not self.is_empty():
            print(f"Popped element: {self.stack.pop()}")
        else:
            print("Stack is empty. Nothing to pop.")

    # Peek 
    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.stack[-1]}")
        else:
            print("Stack is empty.")

    # Check 
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        if not self.is_empty():
            print("Stack contents (top to bottom):", self.stack[::-1])
        else:
            print("Stack is empty.")

# Menu-driven program
def stack_menu():
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter element to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

stack_menu()
