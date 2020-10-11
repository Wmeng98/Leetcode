# Deque is preferred over list in cases where need quicker append and pop operations

# Deque provides O(1) for append/pop whereas list is O(n)

from collections import deque

class Queue:
    # Ctor init queue
    def __init__(self):
        self.queue = deque()

    def isEmpty(self):
        return False if self.queue else True
    def peek(self):
        return self.queue[0]
    def dequeue(self):
        if self.isEmpty():
            return
        # print('dequeue...')
        # print(self.queue)
        self.queue.popleft()
        # print(self.queue)
    def enqueue(self, item):
        self.queue.append(item)
    

# IMPLEMENT A STACK USING A QUEUE
# Can either have a costly pop or push operation

# Impl costly push

# enqueue new item to q2, dequeue from q1 to q2, swap q1, q2 names

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def pop(self):
        if self.q1.isEmpty():
            return
        self.q1.dequeue()

    def push(self, val):
        self.q2.enqueue(val)
        while not self.q1.isEmpty():
            # print(self.q1.queue)
            # print(self.q1.isEmpty())
            # print('asalk')
            # pop and push to q2
            self.q2.enqueue(self.q1.peek())
            self.q1.dequeue()
            # print(self.q1.queue)
        # swap names
        q = self.q1
        self.q1 = self.q2
        self.q2 = q

    def top(self):
        if self.q1.isEmpty():
            return -1 # None instead?
        return self.q1.peek()
    
stack = Stack()
stack.push(34)
stack.push(3)
stack.push(31)
stack.push(98)
stack.push(92)
stack.push(23)

print('stack using queue', stack.q1.queue)



# Generate binary numbers from 1 to n using a queue

# 1, 10, 11, 100, 101, 111
# Think of it as doing a BFS on a tree with 1 as root, root+0 as left child, root+1 as a right child

# 1. Empty queue of strings
# 2. Enqueue first binary num to queue "1"
# 3. Run for loop to gen/print n binary numbers

def genNBinary(n):
    q = Queue()
    q.enqueue("1")

    while n > 0:
        n -= 1
        deq = q.peek()
        q.dequeue()
        print(deq)

        # temp = deq
        # deq += "0"
        q.enqueue(deq+"0")
        q.enqueue(deq+"1")

print('Generate n binary nums:')
genNBinary(5)