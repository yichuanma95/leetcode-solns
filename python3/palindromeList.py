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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        value_list = []
        current = head
        while current:
            value_list.append(current.val)
            current = current.next
        return self.is_list_palindrome(value_list)
    
    def is_list_palindrome(self, vals: [int]) -> bool:
        left = 0
        right = len(vals) - 1
        while left < right and vals[left] == vals[right]:
            left += 1
            right -= 1
        
        return left >= right
