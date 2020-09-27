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
signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        ''' (Solution, int) -> int
        
        Reverse the digits of a given integer. If the given integer is negative, then the
        reversed integer should be negative as well. If the given integer has zeros at the
        end, then the reversed integer should not have the leading zeroes. If the reversed
        integer is outside the 32-bit signed integer range, then zero is returned.
        
        >>> soln = Solution()
        >>> soln.reverse(123)
        321
        >>> soln.reverse(-123)
        -321
        >>> soln.reverse(120)
        21
        >>> soln.reverse(-120)
        -21
        '''
        
        is_negative = x < 0
        reversed_num = self.reverse_num(abs(x))
        
        if -reversed_num < -(2 ** 31) or reversed_num > (2 ** 31) - 1:
            return 0
    
        return -reversed_num if is_negative else reversed_num
        
    def reverse_num(self, x: int) -> int:
        ''' (Solution, int) -> int
        
        Reverse the digits of a given number and return it. If the given number has zeros at
        the end, then the reversed number should not have the leading zeroes.
        
        >>> soln = Solution()
        >>> soln.reverse_num(123)
        321
        >>> soln.reverse_num(120)
        21
        '''
        
        reversed = 0
        
        while x > 0:
            reversed += (x % 10)
            x //= 10
            reversed *= 10
        
        # Because reversed was multiplied by 10 one extra time in the while loop,
        # reversed should be divided by 10 before being returned.
        return reversed // 10
