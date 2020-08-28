'''
Problem 342: Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?

Solution runtime: 12ms, faster than 98.55% of Python submissions
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 4 ** math.ceil(math.log(num, 4)) == num
