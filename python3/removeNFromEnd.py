'''
Problem 19: Remove nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.

Follow up: Could you do this in one pass?

Solution runtime: 28ms, faster than 99.69% of Python3 solutions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current: ListNode = head
        nAway: ListNode = current
        
        for i in range(n):
            nAway = nAway.next
        if nAway is not None:
            if nAway.next is None:
                current.next = current.next.next
                return head
            nAway = nAway.next
        while nAway is not None:
            current = current.next
            nAway = nAway.next
        if current == head:
            head = current.next
        else:
            current.next = current.next.next
        
        return head
