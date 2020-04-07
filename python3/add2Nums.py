'''
Problem 2: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits
are stored in reverse order and each of their nodes contain a single digit. Add the two numbers
and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Solution runtime: 72ms, faster than 92.85% of Python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2
        sumList = None
        newHead = None
        carry = 0
        
        while current1 is not None and current2 is not None:
            tempSum = current1.val + current2.val + carry
            carry = tempSum // 10
            if sumList is None:
                sumList = ListNode(tempSum % 10)
                newHead = sumList
            else:
                sumList.next = ListNode(tempSum % 10)
                sumList = sumList.next
            current1 = current1.next
            current2 = current2.next
        if current1 is not None:
            sumList.next = self.finishAddition(current1, carry)
            carry = 0
        elif current2 is not None:
            sumList.next = self.finishAddition(current2, carry)
            carry = 0
        while sumList.next is not None:
            sumList = sumList.next
        if carry != 0:
            sumList.next = ListNode(carry)
            
        return newHead
    
    def finishAddition(self, l: ListNode, carry: int) -> ListNode:
        prev = None
        head = l
        
        while l is not None:
            tempSum = l.val + carry
            carry = tempSum // 10
            l.val = tempSum % 10
            prev = l
            l = l.next
        if carry != 0:
            prev.next = ListNode(carry)

        return head
