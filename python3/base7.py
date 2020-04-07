'''
Problem 504: Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        isNegative = num < 0
        num = abs(num)
        base7 = ""
        
        while num > 0:
            base7 += str(num % 7)
            num //= 7
        
        if isNegative:
            return "-" + base7[::-1]
        return base7[::-1]
