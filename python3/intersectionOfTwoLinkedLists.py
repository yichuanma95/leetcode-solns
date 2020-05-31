'''
Problem 160: Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
[a1,a2,c1,c2,c3]
[b1,b2,b3,c1,c2,c3]
begin to intersect at node c1. 

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two
lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads
as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before
the intersected node in B. 

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two
lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads
as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before
the intersected node in B. 

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as
[1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can
be arbitrary values.
Explanation: The two lists do not intersect, so return null. 

Notes:
-If the two linked lists have no intersection at all, return null.
-The linked lists must retain their original structure after the function returns.
-You may assume there are no cycles anywhere in the entire linked structure.
-Your code should preferably run in O(n) time and use only O(1) memory.

Solution memory usage: 27.8 MB, less than 100% of Python3 solutions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ''' (Solution, ListNode, ListNode) -> ListNode
        
        Returns the node where the linked lists starting at headA and headB intersect if
        they do, otherwise null.
        '''
        
        # Traverse each list and count the number of node in them.
        node_count_A = self.len_of_linked_list(headA)
        node_count_B = self.len_of_linked_list(headB)
        
        # For the list with more nodes, move its pointer the difference between the
        # lists' lengths.
        len_diff = abs(node_count_A - node_count_B)
        for i in range(len_diff):
            if node_count_A > node_count_B:
                headA = headA.next
            else:
                headB = headB.next
        
        # Simultaneously move both pointers for A and B and see if they point to the same
        # node. If so, the intersecting node has been found.
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # No intersecting node has been found at this point, so the lists don't intersect.
        return None

    def len_of_linked_list(self, head):
        ''' (Solution, ListNode) -> int
        
        Returns the number of nodes that the linked list starting at head contains.
        '''
        
        node_count = 0
        current = head
        
        while current:
            node_count += 1
            current = current.next
        
        return node_count
