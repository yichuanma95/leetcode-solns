'''
Problem 202: Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive
integer, replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Solution runtime: 24ms, faster than 99.77% of Python3 submissions

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        ''' (Solution, int) -> bool
        
        Returns True iff n is a "happy" number, which is a number that results in a 1 after
        a repetitive process of replacing the original number by the sum of digit squares.
        
        >>> soln = Solution()
        >>> soln.isHappy(19)
        True
        '''
        
        # This set will store all the unique sum of digit squares generated while
        # determining if n is "happy".
        unique_digit_square_sums = set()
        
        # Keep calculating the sum of digit squares until it's equal to 1, in this case
        # return True, or it already is in the set, in this case return False.
        while n not in unique_digit_square_sums:
            unique_digit_square_sums.add(n)
            n = self.sum_of_digit_squares(n)
            if n == 1:
                return True
        
        return False
        
    def sum_of_digit_squares(self, n):
        ''' (Solution, int) -> int
        
        Calculates and returns the sum of squares of n's digits.
        
        >>> soln = Solution()
        >>> soln.sum_of_digit_squares(19)
        82
        >>> soln.sum_of_digit_squares(82)
        68
        '''
        
        digit_square_sum = 0
        
        while n > 0:
            digit_square_sum += ((n % 10) ** 2)
            n //= 10
        
        return digit_square_sum
