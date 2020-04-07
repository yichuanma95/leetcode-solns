'''
Problem 202: Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive
integer, replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Solution runtime: 24ms, faster than 99.77% of Python3 submissions

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        numSet.add(n)
        
        while n != 1:
            k = n
            temp = 0
            while k > 0:
                temp += (k % 10) ** 2
                k //= 10
            n = temp
            if n in numSet:
                return False
            numSet.add(n)
        
        return True
