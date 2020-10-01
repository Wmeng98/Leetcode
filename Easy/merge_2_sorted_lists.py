# Solution 1 - Recursive Approach
# Recursivelly define the merge of two lists as the following...
#   Smaller of the two head nodes plus to result of the merge on the rest of the nodes
# Time 0(n+m) and Space O(n+m) -> first recursive call doesn't return untill ends of l1 && l2 have been reached


# Solution 2 - Iterative Approach
# Can achieve the same idea via iteration
# Insert elements of l2 in necessary places of l1
# Need to setup...
#  A false prehead to return the head of merged list
#  prev - node we will be adjusting the next ptr of
#  Stop comparison until one of l1 or l2 points to null

# Time O(n+m) Space O(1) - only alloc a few pointers


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    prehead = ListNode(-1)
    prev = prehead
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    # connect non-null list to end of merged list
    prev.next = l1 if l1 is not None else l2
    return prehead.next
