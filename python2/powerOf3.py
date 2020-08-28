'''
Problem 326: Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up: Could you do it without using any loop / recursion?

Solution runtime: 52ms, faster than 98.5% of Python submissions
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** math.ceil(math.log(n, 3)) == n
