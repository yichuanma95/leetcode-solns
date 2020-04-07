'''
Problem 476: Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the
bits of its binary representation.

Notes:
1. The given integer is guaranteed to fit within the range of a 32-bit signed integer.
2. You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement
is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0.
So you need to output 0.

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

import math

class Solution:
    def findComplement(self, num: int) -> int:
        bits = bin(num)[2:]
        complement = 0
        
        for b in bits:
            complement += (1 if b == '0' else 0)
            complement <<= 1
        
        return complement >> 1
