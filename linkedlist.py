class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert at beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert at specific position
    def insertAtPosition(self, data, position):
        if position == 0:
            self.insertAtBegin(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Index out of range")
                return
            current_node = current_node.next
        if current_node is None:
            print("Index out of range")
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    # insert at end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # Update node of a linked list at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # remove at first
    def removeFirstNode(self):
        if self.head is not None:
            self.head = self.head.next

    # delete at last
    def removeLastNode(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    # Method to remove at given index
    def removeAtIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            self.removeFirstNode()
            return
        current_node = self.head
        position = 0
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # delete at given position
    def removeNode(self, data):
        current_node = self.head
        if current_node is None:
            return
        if current_node.data == data:
            self.removeFirstNode()
            return
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is not None:
            current_node.next = current_node.next.next

    # display linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # length of linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
