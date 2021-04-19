# 
# 
# STACKS - LIFO
# 
# 

'''
Stack implementation

NOTE: Stacks can be used to implement recursive algorithm iteratively
'''
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    
    def isEmpty(self):
        return False if self.stack else True
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def push(self, data):
        self.stack.append(data)
    
    def evalPostfix(self, exp):
        # iterate over expression for conversion
        for i in exp:
            # isdigit only for positive unsigned integers
            if i.isdigit():
                # could convert to int here too
                self.push(i)
            else:
                # pop two elements and apply operator
                v1 = self.pop()
                v2 = self.pop() 
                # string parsing here is, don't parse str for multi-digits tho
                res = str(eval(v2 + i + v1))
                self.push(res)
        return int(self.pop())

'''
[Evaluate postfix expression using a stack]

The sol'n is to create a stack to store operands

Soln: Scan expr and do the following
    1. If number, push onto stack
    2. If operand, pop numbers (2) from stack, eval operator, push back onto stack

[RUNTIME] O(n) -> n length of string
[COMPLEXITY] O(n)
    
'''

psf = Stack()
exp = "231*+9-"
print('postfix:', psf.evalPostfix(exp))



'''
[Sort values in stack in descending order]

Use temp stack- return tmp stack
O(n^2)
'''

def sortStack(stack):
    print(stack.stack)
    # temp stack to hold sorted vals
    tmpStack = Stack()

    # while stack isn't empty
    while not stack.isEmpty():
        tmp = stack.pop()

        # insert into sorted pos in tmpStack
        while not tmpStack.isEmpty() and tmpStack.peek() > tmp:
            stack.push(tmpStack.pop())
        tmpStack.push(tmp)
    return tmpStack

stack = Stack()
stack.push(34)
stack.push(3)
stack.push(31)
stack.push(98)
stack.push(92)
stack.push(23)

sortedStack = sortStack(stack)
print('sortStack', sortedStack.stack)


'''
[Implement stack using queues]

2 methods
    1. make push operation costly
    2. make pop operation costly

'''

class Stack2():
    def __init__(self):
        # q1 is primary queue
        # enqueue from left, dequeue from right
        self.q1 = deque()
        self.q2 = deque()
    def isEmpty(self):
        return False if self.q1 else True
    def peek(self):
        # check is empty first
        return self.q1[0]
    def push(self, d):
        self.q1.appendleft(d)
    # make dequeue costly
    def pop(self):
        # dequeue all but the last item from q1 into q2
        # dequeue and return last item in q1 
        # swap primary queue to q2 (swap)

        # TODO: check isEmpty edge case
        while len(self.q1) > 1:
            self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.pop()        

stack = Stack2()
stack.push(34)
stack.push(3)
stack.push(31)
stack.push(98)
stack.push(92)
stack.push(23)

# expect 23, 92, 98, ...
print('impl stack with 2 queues (23, 92, 98...)', stack.pop(), stack.pop(), stack.pop(), '...')


# 
# 
# QUEUES - FIFO
# 
# 

'''
Queue implementation

NOTE: Used in BFS to process nodes in order which they are viewed
'''

class Queue():
    def __init__(self):
        # append from left, remove from right
        self.queue = deque()
    def isEmpty(self):
        return False if self.queue else True
    def peek(self):
        return self.queue[-1]
    def enqueue(self, d):
        self.queue.appendleft(d)
    def dequeue(self):
        if self.isEmpty():
            return
        return self.queue.pop()

'''
[Implement stack with 2 queues] -> See above ^
'''

'''
[Implement queue with 2 stacks]

2 methods
    1. enqueue is costly
    2. dequeue is costly
'''

'''
[Generate binary numbers from 1 to n using a queue]

 1,10,11,100,101,111,...

 Think of it as doing BFS on tree with 1 as root, root+0 as left && root+1 as right child

 [RUNTIME] O(n) -> wrt to nth binary number
 [SPACE] O(n) -> worst case hold all vertices in the queue (think of a case!)

'''

def genNBinary(n):
    q = Queue()
    q.enqueue("1")

    while n > 0:
        n -= 1
        deq = q.peek()
        q.dequeue()
        print(deq)

        q.enqueue(deq+"0")
        q.enqueue(deq+"1")

print('Generate n binary nums:')
genNBinary(5)