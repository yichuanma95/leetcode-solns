'''
Problem 21: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1: ListNode = l1
        current2: ListNode = l2
        prev1: ListNode = None
        prev2: ListNode = None
        merged: ListNode = None
        newHead: ListNode = None
        
        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                prev1 = current1
                current1 = current1.next
                prev1.next = None
                if merged is None:
                    merged = prev1
                else:
                    merged.next = prev1
                    merged = merged.next
            else:
                prev2 = current2
                current2 = current2.next
                prev2.next = None
                if merged is None:
                    merged = prev2
                else:
                    merged.next = prev2
                    merged = merged.next
            if newHead is None:
                newHead = merged
        if current1 is not None:
            if merged is None:
                return current1
            merged.next = current1
        if current2 is not None:
            if merged is None:
                return current2
            merged.next = current2

        return newHead
