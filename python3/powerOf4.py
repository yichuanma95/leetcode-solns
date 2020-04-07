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

Solution runtime: 24ms, faster than 91.75% of Python3 submissions

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        
        return 4 ** math.floor(math.log(num, 4)) == num
