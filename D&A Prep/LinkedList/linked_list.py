# [Reverse a linked list - LEETCODE EASY]

# 2 ways of doing this, iterative and recursive

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode():
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def push(self, data):
        node = ListNode(data)
        # new head node
        node.next = self.head
        self.head = node
    # Utility function to print it 
    # the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.val, end =" ") 
            temp = temp.next
        


def reverseList(head):
    # check edge case
    if head is None:
        return head
    
    # set curr.next = prev and reposition for next iteration
    prev = None
    currr = head
    while curr is not None:
        next = curr.next # remember the next node
        # current nodes next pointer will be made to point to its previous node
        curr.next = prev
        
        prev = curr # used in next iteration, move to next node
        curr = next # Move to next node
    return prev



# With recursive solution, key is to work backwards

#
# Assume from node nk+1 to nm had been reversed and you are at node nk.
# n1 → … → nk-1 → nk → nk+1 ← … ← nm
# We want nk+1’s next node to point to nk.
#

def reverseListRecursive(head):
    # Base cases
    if (head is None or head.next is None):
        return head
    # recurse on head.next node
    p = reverseListRecursive(head.next)
    # Not tail recursive because last instr in this functon isn't the recursive call
    
    # Want next node of head to point to head
    head.next.next = head
    head.next = null
    
    # return the new head after reversal
    return p




# [DETECT LOOP IN A LINKED LIST]

''' 
Can use hash map - linear space
Modify the nodes with a flag

Floyd's Cycle-Finding Algorithm -> Fastest method

'''

def cycleDetection(head):
    # slow and fast pointers
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # == compares values of objects
        # is checks if same instance
        if slow is fast:
            return True
    return False
            


# COPIED FROM GEEKSFORGEEKS

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
   
# Create a loop for testing 
llist.head.next.next.next.next = llist.head; 
  
if(cycleDetection(llist.head)): 
    print ("Loop found") 
else : 
    print ("No Loop ") 


# [FOLLOW UP QUESTION - Detect first node of loop in a linked list]

# Hash Table - Easiest but O(n) space

# Floyd's Cycle
'''
m - distance of the first node of the cycle from the head
n - length of the cycle
k - distance of node where slow and fast meet from first node in loop

can conclude that distance travelled by fast ptr = 2*(distance travelled by the slow ptr)
(m + xn + k) = 2*(m + yn + k)

where...
x - number of complete cyclic rounds made by the fast ptr
y - number of complete cyclic rounds made by the slow ptr

therefore...
m + k = (x-2y)n

m + k is a multiple of n

Algorithm
- find meeting point - meet
- now start moving ptrs at same speed one starting at head and one at meet.
- bc m + k is a multiple of n, after m steps, meet at beginning of the loop

'''

# Impl left as an exercise for myself :)




# [Return Nth node from the end in a linked list]

# Method 1 - Use the length of the linked list - print (len - n + 1) from begin of LL
# Method 2 - Use 2 pointers, move ref ptr to n nodes from head

def printNthFromLast(head, n):
    main = head
    ref = head

    # first move ref n steps
    steps = 0
    while steps < n:
        if ref.next is None:
            print('N steps greater than number of nodes in LL')
            return
        # o/w step and update
        ref = ref.next
        steps += 1
    
    while ref.next is not None:
        # move main and ref forward by 1 until end of LL reached
        main = main.next
        ref = ref.next
    
    # print main node
    print('Nth node %d from end has value %d' % (n, main.val))

# Bill.com interview question
'''
Method 1 - put into an array and index the middle A.lengh // 2
Method 2 - Fast and slow pointer
'''
def printMidNode(head):
    main = head
    ref = head
    if ref is None:
        print('Empty LL')
        return
    
    # until we reach the end of the list
    while ref and ref.next:
        main = main.next
        ref = ref.next.next
    
    print('Middle node has value %d' % main.val)
        



# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
   
print('printNthFromLast')
printNthFromLast(llist.head, 0)
printNthFromLast(llist.head, 1)
printNthFromLast(llist.head, 2)
printNthFromLast(llist.head, 3)
printNthFromLast(llist.head, 4)
printNthFromLast(llist.head, 5)
print('')
print('printMidNode')
printMidNode(llist.head)
        



# [Remove duplicates from a linked list]

'''
If sorted, can remove in linear time

O/W can do the following

Method1: Sort and then remove in linear time
Method2: Hashing

'''

# Use hashing
def removeDuplicates(head):
    cMap = {}
    
    curr = head
    # catch empty list
    cMap[curr.val] = True

    while curr and curr.next is not None:
        # print(curr.val)
        # print(cMap)
        # store val in cMap
        if curr.next.val not in cMap:
            cMap[curr.next.val] = True
            curr = curr.next
        else:
            # remove duplicate and don't update curr
            curr.next = curr.next.next
        # curr = curr.next
    return head

# Driver program for testing 
llist = LinkedList() 
llist.push(10)
llist.push(20) 
llist.push(4) 
llist.push(20)
llist.push(15)
llist.push(10)
llist.push(10)
llist.push(10) 
llist.push(10)
llist.push(15)
llist.push(4) 
print('removeDuplicates')
removeDuplicates(llist.head)
llist.printList()
