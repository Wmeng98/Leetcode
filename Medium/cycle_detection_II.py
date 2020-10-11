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


# [FOLLOW UP QUESTION - Detect first node of loop in a linked list - MEDIUM]

# Hash Table - Easiest but O(n) space

# Floyd's Cycle
'''
m - distance of the first node of the cycle from the head
n - length of the cycle
k - distance of node where slow and fast meet

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