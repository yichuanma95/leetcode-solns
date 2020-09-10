'''
Problem 367: Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square,
otherwise False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    # The O(log n) solution that uses binary search.
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        
        return self.binSearch(0, num, num)
    
    def binSearch(self, lo, hi, num):
        if lo > hi:
            return False
        
        mid = (lo + hi) // 2
        square = mid * mid
        
        if square == num:
            return True
        if square < num: # search right
            return self.binSearch(mid + 1, hi, num)
        return self.binSearch(lo, mid - 1, num)

    # The O(sqrt(n)) solution
    def isPerfectSquare_v2(self, num: int) -> bool:
        i = 1
        while i ** 2 < num:
            i += 1
        return i ** 2 == num
    