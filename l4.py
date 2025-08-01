# Simulate a basic stack and queue using a list

def stack_menu():
    stack = []
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit Stack Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            val = input("Enter value to push: ")
            stack.append(val)
            print(f"Pushed {val}")
        elif choice == '2':
            if stack:
                print(f"Popped {stack.pop()}")
            else:
                print("Stack is empty!")
        elif choice == '3':
            print("Stack:", stack)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

def queue_menu():
    queue = []
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit Queue Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            val = input("Enter value to enqueue: ")
            queue.append(val)
            print(f"Enqueued {val}")
        elif choice == '2':
            if queue:
                print(f"Dequeued {queue.pop(0)}")
            else:
                print("Queue is empty!")
        elif choice == '3':
            print("Queue:", queue)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

while True:
    print("\nMain Menu:")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Exit")
    main_choice = input("Enter your choice: ")
    if main_choice == '1':
        stack_menu()
    elif main_choice == '2':
        queue_menu()
    elif main_choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
