'''
Problem 231: Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false

Solution runtime: 16ms, faster than 94.11% of Python submissions
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n & 1 == 0 and n > 0:
            n >>= 1
            
        return n == 1
