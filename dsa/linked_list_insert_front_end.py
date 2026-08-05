class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
current = None


def insert_end(data):
    global head, current
    if head is None:
        head = Node(data)
        current = head
    else:
        current.next = Node(data)
        current = current.next


def insert_front(data):
    global head, current
    if head is None:
        head = Node(data)
        current = head
    else:
        node = Node(data)
        node.next = head
        head = node


def print_nodes():
    trav = head
    while trav is not None:
        print(trav.data, "-->", end="")
        trav = trav.next
    print("null")


if __name__ == "__main__":
    for i in range(5):
        insert_front(int(input("Enter the node data at front: ")))
        insert_end(int(input("Enter the node data at end: ")))
    print_nodes()
