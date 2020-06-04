'''
Problem 24: Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

Solution runtime: 16ms, faster than 99.74% of Python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        
        if not current or not current.next:
            return head
        
        while current:
            if not current.next:
                break
            temp = current.next
            current.next = current.next.next
            temp.next = current
            if not prev:
                head = temp
            else:
                prev.next = temp
            prev = current
            current = current.next
        
        return head
