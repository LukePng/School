class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

# fixed size = 10
class ArrayQueue:
    CAPACITY = 10 # class-variable

    def __init__(self):
        self.data = [''] * ArrayQueue.CAPACITY
        self.tail = -1
        # self.head not needed as it is always at 0 (unless no queue)
        # depends on question whether head is needed

    def enqueue(self, data):
        if self.tail == ArrayQueue.CAPACITY -1: # tail is pointing to the last item
            print("Queue is full.")
            return # exit the enqueue
        
        else:
            self.tail += 1 # move the tail pointer down
            self.data[self.tail] = data # add data to position of tail

    def dequeue(self):
        if self.tail == -1: # tail is pointing at None
            return "Queue is empty."
        
        else:
            ret = self.data[0] # first item in the queue

            for idx in range(self.tail): # tail corresponds to the number of items in the queue
                self.data[idx] = self.data[idx+1] # shift every element up
            self.tail -= 1 # move tail pointer up by 1

            return ret
        
    def __len__(self):
        return self.tail + 1
    
    def display(self):
        psn = 1
            
        for data in self.data[0:self.tail+1]:
            print(f"{psn}. {data}")
            psn += 1

canteen = ArrayQueue()

canteen.enqueue("1")
canteen.enqueue("2")
canteen.enqueue("3")

# print(canteen.dequeue())
# print(canteen.dequeue())
# print(canteen.dequeue())

canteen.display()

print(len(canteen))