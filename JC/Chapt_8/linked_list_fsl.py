class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    def push(self, data = Node()):
        data.next = self.root
        self.root = data

    def insert(self, data: Node, position):
        if position == 0:
            data.next = self.root
            self.root = data
        else:
            count = 0
            ptr = self.root
            while ptr.next is not None:
                if count == position:
                    data.next = ptr.next
                    ptr.next = data
                    return
                else:
                    count += 1
                    ptr = ptr.next
    
    def delete(self, target):
        if self.root is None:
            print("Linked list is empty!")
            return
        else:
            ptr = self.root
            while ptr.next is not None:
                if ptr.next == target:
                    ptr = ptr.next.next
                    return
                else:
                    ptr = ptr.next

            print("Target not found, no nodes removed!")
            return
    
class Toilet:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.data = LinkedList()
        self.fsl = LinkedList()
        
    def build_toilet(self):
        for i in range(self.capacity):
            self.fsl.push()

    def piss(self, data: Node, position):
        self.fsl.root = data.data
        temp_node = self.fsl.root
        self.fsl.root = temp_node.next
        self.root.insert(temp_node, position)

        

                        


