'''
Problem 83: Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3

Solution runtime: 40ms, faster than 98.11% of Python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        current: ListNode = head
        
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
