'''
Problem 234: Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodeStack = []
        current: ListNode = head
        nodes: int = 0
        count: int = 1
        
        while current is not None:
            nodes += 1
            current = current.next
        current = head
        half: int = nodes // 2
        
        while count <= half:
            print(current.val)
            nodeStack.append(current.val)
            count += 1
            current = current.next
        if nodes % 2 != 0:
            current = current.next
        while current is not None:
            if current.val != nodeStack[-1]:
                return False
            else:
                nodeStack.pop()
            current = current.next

        return True
