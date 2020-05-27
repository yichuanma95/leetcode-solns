'''
Problem 70: Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # This problem is basically finding the (n+1)th Fibonacci number so below is
        # an implementation of Binet's formula, which can calculate the nth Fibonacci number
        # in constant time.
        sqrt_5 = math.sqrt(5)
        phi = (1 + sqrt_5) / 2
        psi = (1 - sqrt_5) / 2
        n_plus_1 = n + 1
        
        return math.floor(((phi ** n_plus_1) - (psi ** n_plus_1)) / sqrt_5)
