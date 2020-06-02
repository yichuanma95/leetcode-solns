'''
Problem 171: Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701

Solution runtime: 20ms, faster than 99.57% of Python3 submissions

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        ''' (Solution, str) -> int
        
        Returns the index number for the given Excel sheet column title.
        
        >>> soln = Solution()
        >>> soln.titleToNumber('A')
        1
        >>> soln.titleToNumber('AB')
        28
        >>> soln.titleToNumber('ZY')
        701
        '''
        
        # This variable will store the final column index number
        col_index = 0
        
        # Iterate through s in reverse
        for i, c in enumerate(s[::-1]):
            # For each char, add 26 ^ (char_index) * (ASCII value of char) - 64 to the column
            # index number, where 64 is 1 less than the ASCII value of 'A' (65)
            col_index += (26 ** i * (ord(c) - 64))
        
        return col_index
