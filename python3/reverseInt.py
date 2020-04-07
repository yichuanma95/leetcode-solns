'''
Problem 7: Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        y = x % 10
        
        x //= 10
        while x > 0:
            y *= 10
            y += (x % 10)
            x //= 10
        if neg:
            y *= -1
        if y > (2**31 - 1) or y < (2**31) * -1:
            return 0

        return y
