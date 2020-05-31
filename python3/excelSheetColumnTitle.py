'''
Problem 168: Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"

Solution runtime: 24ms, faster than 91.9% of Python3 submissions
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        ''' (Solution, int) -> str
        
        Precondition: n >= 1
        
        Returns the title for the nth column in an Excel sheet. The title is upper-case.
        
        >>> soln = Solution()
        >>> soln.convertToTitle(1)
        'A'
        >>> soln.convertToTitle(28)
        'AB'
        >>> soln.convertToTitle(701)
        'ZY'
        '''
        
        # This string collects the letters for the column title.
        col_title = ''
        
        # While n > 0, the next letter is the letter at (n - 1) % 26. Then n = (n - 1) // 26
        while n > 0:
            col_title += chr(65 + (n - 1) % 26)
            n = (n - 1) // 26
        
        # At this point, the column title is in reverse. Reverse it then return it.
        return col_title[::-1]
    