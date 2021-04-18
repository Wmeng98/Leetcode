'''

[LINKED LISTS]

Constant time add/remove
Memory doesn't need to be contiguous/consecutive

'''

class ListNode():
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    '''
    INSERT NODE INTO LINKED LIST AT BEGINNING
    '''
    def push(self, data):
        # Insert node at beginning
        node = ListNode(data)
        node.next = self.head
        self.head = node
    
    def printList(self):
        temp = self.head
        
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print('\n')

def createTestList():
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    
    return llist


'''

Reversing a Linked List

Iterative vs. recursive (O(n) stack space if not tail recursive)

'''

def reverseList(head):
    # check edge case
    if head is None:
        return head
    
    # set curr.next = prev and reposition for next iteration
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        
        prev = curr
        curr = next

    return prev

# NOT TAIL RECURSION
def recursiveReverse(head): 
    # work backwards,
    # Assume from node nk+1 to nm had been reversed and you are at node nk.
    # n1 → … → nk-1 → nk → nk+1 ← … ← nm
    # We want nk+1’s next node to point to nk.

    # base cases , return reversed head in recursion
    if head is None or head.next is None:
        return head
    
    p = recursiveReverse(head.next)

    head.next.next = head
    head.next = None

    return p

# TAIL RECURSION - operate first, then call reverse(curr=next,prev=curr)
    # NOTE: No longer working backwards here, same as iterative

# driver program to test
lst = createTestList()
lst.head = reverseList(lst.head)
print('iterative reverse llist')
lst.printList()
lst = createTestList()
lst.head = recursiveReverse(lst.head)
print('recursive reverse llist')
lst.printList()

'''
DELETING A NODE

find prev node and set prev.next = n.next
if doubly linked, set n.next.prev = n.prev

'''
def deleteNode(head, d):
    if head.val == d:
        head = head.next
    
    curr = head
    while curr.next is not None:
        if curr.next.val == d:
            curr.next = curr.next.next
            return head
        curr = curr.next
    return head

################################################################################################################################################################

'''

DETECT CYCLE IN LINKED LIST

Can use hash map - linear space
Modify the nodes with a flag

Floyd's Cycle-Finding Algorithm -> Fastest method

[RUNTIME] find start node only need m steps so O(n)
[SPACE] O(1) space

'''

def cycleDetection(head):
    # slow and fast pointers
    slow = fast = head
    # slow is not None and fast is not None and fast.next is not None
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def cycleDetectionStartNode(head):
    slow = fast = head
    cycle = False
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            cycle = True
            break
    if not cycle:
        return None
    
    # move slow back to head and inc both by 1 until get collision (start of cycle)
    i = head
    j = fast
    while i is not j:
        i = i.next
        j = j.next
    return i

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
   
# Create a loop for testing 
llist.head.next.next.next.next = llist.head; 
node = cycleDetectionStartNode(llist.head)
print('cycle detection at node', node, 'with val', node.val)
    

################################################################################################################################################################

'''

[Return Nth node from the end in a linked list]

# Method 1 - Use the length of the linked list - print (len - n + 1) from begin of LL
# Method 2 - Use 2 pointers, move ref ptr to n nodes from head

[RUNTIME] O(n)
[SPACE] O(1)

'''

def printNthFromLast(head, n):
    main = head
    ref = head

    #  first move ref n steps
    steps = 0
    while steps < n:
        if ref.next is None:
            print('N steps greater than number of nodes in LL')
            return
        ref = ref.next
        steps += 1
    # move both ptrs forward by 1 until end of LL reached
    while ref.next is not None:
        main = main.next
        ref = ref.next
    
    # print main node
    print('Nth node %d from end has value %d' % (n, main.val))

################################################################################################################################################################

'''
Print Middle node

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
        

################################################################################################################################################################

'''

[REMOVE DUPLICATES FROM A LINKED LIST]

If sorted, can remove in linear time

O/W can do the following

Method1: Sort and then remove in linear time
Method2: Hashing 
    --> can still hash and remove in one pass

'''

def removeDuplicates(head):
    cMap = {}
    curr = head
    # NOTE: catch empty list
    
    cMap[curr.val] = True
    while curr and curr.next:
        if curr.next not in cMap:
            cMap[curr.next.val] = True
            curr = curr.next
        else:
            # remove dup, don't update curr
            curr.next = curr.next.next
    return head 


################################################################################################################################################################
################################################################################################################################################################
'''

Singly vs. Doubly Linked List

Single:
    Complexity: insert/delete at known position O(n)
    Usage: stacks
    index perf: when need to save memory and search not required
Double
    Complexity: insert/delete at known position O(1)
    Usage: stacks, heaps, binary trees
    index perf: if searching required and memory is not a limitation (2 ptr per node not 1 anymore)

'''

################################################################################################################################################################