# Evaluate postfix expression using a stack

# Create stack to store operands (values)
# Scan expression and do followiing...
#   1. Number, push onto stack
#   2. Operator, Pop operands from stack, eval operator, and push back onto the stack
from collections import deque
class Postfix:
    # Constructor to init stack
    def __init__(self):
        self.stack = deque()
    
    def isEmpty(self):
        return False if self.stack else True
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def push(self, operand):
        self.stack.append(operand)
    
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

psf = Postfix()
exp = "231*+9-"
print('postfix:', psf.evalPostfix(exp))
                


class Stack:
    # Constructor to init stack
    def __init__(self):
        self.stack = deque()
    
    def isEmpty(self):
        return False if self.stack else True
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def push(self, operand):
        self.stack.append(operand)
    
    def getDeque(self):
        return self.stack


# Sort values in stack in descending order
# Use a temp stack
# O(n^2)

def sortStack(stck):
    # Create a tmp stack to hold sorted values of stack
    tmpStack = Stack()

    while not stck.isEmpty():
        # pop from stack and store as tmp
        tmp = stck.pop()

        # while tmpStack top is greater than tmp
        while (not tmpStack.isEmpty()) and tmpStack.peek() > tmp:
            stck.push(tmpStack.peek())
            tmpStack.pop()
        
        # push tmp onto tmpStack in sorted order
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
print('sortStack', sortedStack.getDeque())


# Valid Parentheses

            