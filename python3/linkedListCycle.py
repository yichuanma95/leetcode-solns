'''
Problem 141: Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the
position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is
no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Solution runtime: 48ms, faster than 93.48% of Python3 submissions

Solution memory usage: 15.5 MB, less than 100% of Python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sentinel = float("Inf")
        current: ListNode = head
            
        while current is not None:
            if current.val == sentinel:
                return True
            current.val = sentinel
            current = current.next
        
        return False
