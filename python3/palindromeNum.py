'''
Problem 9: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the
same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it
is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ''' (Solution, int) -> bool
        
        Return True iff x is a palindrome. A negative number is not a palindrome.
        
        >>> soln = Solution()
        >>> soln.isPalindrome(121)
        True
        >>> soln.isPalindrome(-121)
        False
        >>> soln.isPalindrome(10)
        False
        '''
        
        # Check if x is negative. If it is, it's not a palindrome.
        if x < 0:
            return False
        
        # Reverse x
        x_reversed = self.reverse_num(x)
        
        # Check if x is a palindrome
        return x == x_reversed
        
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

