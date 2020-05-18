'''
Problem 66: Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and
each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ''' (Solution, list of int) -> list of int
        
        Return a list of digits representing a number that is one higher than the
        number represented by digits.
        
        >>> soln = Solution()
        >>> soln.plusOne([1, 2, 3])
        [1, 2, 4]
        >>> soln.plusOne([4, 3, 2, 1])
        [4, 3, 2, 2]
        >>> soln.plusOne([9])
        [1, 0]
        '''
        
        # Add one to the last digit in digits.
        digits_len = len(digits)
        if not self.increment_digit(digits, digits_len - 1, 1):
            return digits
        
        # in case the last digit in the original array was a 9
        for i in range(digits_len - 2, -1, -1):
            if not self.increment_digit(digits, i, 1):
                break
        
        return digits

    def increment_digit(self, digits, i, carry):
        ''' (Solution, list of int, int, int) -> bool
        
        Increments the value at digits[i]. If i=0 and digits[i] was originally 0, then a 1
        is inserted to the beginning of digits. Returns True if the original value
        at digits[i] was a 9, resulting in a nonzero carry value.
        
        >>> soln = Solution()
        >>> xs = [1, 2, 3]
        >>> soln.increment_digit(xs, 2, 1)
        False
        >>> xs
        [1, 2, 4]
        >>> ys = [9]
        >>> soln.increment_digit(ys, 0, 1)
        True
        >>> ys
        [1, 0]
        '''
        
        new_digit = digits[i] + carry
        digits[i] = new_digit % 10
        carry = new_digit // 10
        
        if i == 0 and carry != 0:
            digits.insert(0, carry)
        
        return carry != 0
