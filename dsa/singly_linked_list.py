class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
current = None


def insert(data):
    global head, current
    if head is None:
        head = Node(data)
        current = head
    else:
        current.next = Node(data)
        current = current.next


def print_nodes():
    trav = head
    while trav is not None:
        print(trav.data, "-->", end="")
        trav = trav.next
    print("null")


if __name__ == "__main__":
    for i in range(5):
        insert(int(input("Enter the node data: ")))
    print_nodes()
