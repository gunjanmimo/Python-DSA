class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode: Node):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.ref is None:
                    break
                lastNode = lastNode.ref
            lastNode.ref = newNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)

            currentNode = currentNode.ref
        print("_" * 20)

    def insertAtHead(self, newNode: Node):
        temp = self.head
        self.head = newNode
        self.head.ref = temp

    def insertAt(self, newNode: Node, index: int):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == index:
                previousNode.ref = newNode
                previousNode.ref.ref = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.ref
            currentPosition += 1

    def insertAtTail(self, newNode: Node):
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while True:
            if current_node.ref is None:
                break
            current_node = current_node.ref
        current_node.ref = newNode

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next = current_node.ref
            current_node.ref = prev_node
            prev_node = current_node
            current_node = next
        return prev_node


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    first_node = Node("Gunjan")
    linkedList.insert(first_node)
    second_node = Node("Ben")
    linkedList.insert(second_node)
    third_node = Node("John")
    linkedList.insert(third_node)
    linkedList.printList()

    # INSERTING NEW HEAD
    new_head_node = Node("Paul")
    linkedList.insertAtHead(newNode=new_head_node)
    linkedList.printList()
    new_node = Node("Mimo")
    linkedList.insertAt(new_node, 2)
    linkedList.printList()

    newTail = Node("LA")
    linkedList.insertAtTail(newTail)
    linkedList.printList()

    reverse_linked_list = linkedList.reverse()

    linkedList.head = reverse_linked_list
    linkedList.printList()
