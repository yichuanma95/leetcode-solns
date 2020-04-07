'''
Problem 203: Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

Solution memory usage: 15.6 MB, less than 100% of Python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current: ListNode = head
        prev: ListNode = None
        
        while current is not None:
            if current.val == val:
                if prev is None:
                    head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return head
