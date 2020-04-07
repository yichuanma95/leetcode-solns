'''
Problem 461: Hamming Distance

The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 2^31.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y
        dist = 0

        while val > 0:
            dist += (val & 1)
            val >>= 1
        
        return dist
    