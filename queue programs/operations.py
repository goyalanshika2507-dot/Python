# Queue Implementation using List

queue = []

# Enqueue operation
def enqueue():
    element = input("Enter element to insert: ")
    queue.append(element)
    print("Element inserted")

# Dequeue operation
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        print("Removed element:", queue.pop(0))

# Peek operation
def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

# Display queue
def display():
    print("Queue elements:", queue)

# Menu-driven program
while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")



