queue = []

while True:
    print("\n----- Customer Service Queue -----")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Waiting Customers")
    print("4. Display Front Customer")
    print("5. Display Total Customers")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer = input("Enter Customer Name: ")
        queue.append(customer)
        print(customer, "added to the queue.")

    elif choice == 2:
        if not queue:
            print("No customers to serve.")
        else:
            print(queue[0], "has been served.")
            queue.pop(0)

    elif choice == 3:
        if not queue:
            print("No waiting customers.")
        else:
            print("Waiting Customers:")
            for customer in queue:
                print(customer)

    elif choice == 4:
        if not queue:
            print("Queue is Empty")
        else:
            print("Front Customer:", queue[0])

    elif choice == 5:
        print("Total Customers:", len(queue))

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
