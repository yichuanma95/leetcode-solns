'''
Problem 13: Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve
is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which
is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral
for four is not IIII. Instead, the number four is written as IV. Because the one is before the
five we subtract it making four. The same principle applies to the number nine, which is written
as IX. There are six instances where subtraction is used:

-I can be placed before V (5) and X (10) to make 4 and 9. 
-X can be placed before L (50) and C (100) to make 40 and 90. 
-C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from
1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Solution runtime: 36ms, faster than 96.93% of Python3 submissions
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ''' (Solution, str) -> int
        
        Return the integer representation of a Roman numeral.
        
        >>> soln = Solution()
        >>> soln.romanToInt("III")
        3
        >>> soln.romanToInt("IV")
        4
        >>> soln.romanToInt("IX")
        9
        >>> soln.romanToInt("LVIII")
        58
        >>> soln.romanToInt("MCMXCIV")
        1994
        '''
        
        # length of s should only be calculated once here.
        final_index = len(s) - 1
        final_int = 0
        
        for i in range(final_index + 1):
            final_int += self.value_of_symbol(s, i, final_index)
        
        return final_int
        
    def value_of_symbol(self, s: str, i: int, final_index: int) -> int:
        ''' (Solution, str, int, int) -> int
        
        Return the integer value of the Roman numeral symbol at index i in s.
        
        >>> soln = Solution()
        >>> soln.value_of_symbol("III", 0, 2)
        1
        >>> soln.value_of_symbol("MCMXCIV", 1, 6)
        -100
        >>> soln.value_of_symbol("MCMXCIV", 2, 6)
        1000
        '''
        
        if s[i] == 'I':
            return self.value_of_I(s, i, final_index)
        if s[i] == 'V':
            return 5
        if s[i] == 'X':
            return self.value_of_X(s, i, final_index)
        if s[i] == 'L':
            return 50
        if s[i] == 'C':
            return self.value_of_C(s, i, final_index)
        if s[i] == 'D':
            return 500
        if s[i] == 'M':
            return 1000
        
    def value_of_I(self, s: str, i: int, final_index: int) -> int:
        ''' (Solution, str, int, int) -> int
        
        If I comes before a V or an X, return -1. Otherwise, return 1.
        
        >>> soln = Solution()
        >>> soln.value_of_I("III", 0, 2)
        1
        >>> soln.value_of_I("III", 2, 2)
        1
        >>> soln.value_of_I("IV", 0, 1)
        -1
        '''
        
        # Check if this I comes before a V or an X
        if i < final_index and s[i+1] in ['V', 'X']:
            return -1
        
        return 1
    
    def value_of_X(self, s: str, i: int, final_index: int) -> int:
        ''' (Solution, str, int, int) -> int
        
        If X comes before a L or a C, return -10. Otherwise, return 10.
        
        >>> soln = Solution()
        >>> soln.value_of_X("XX", 0, 1)
        10
        >>> soln.value_of_I("MCMXCIV", 3, 6)
        -10
        '''
        
        # Check if this X comes before a L or a C
        if i < final_index and s[i+1] in ['L', 'C']:
            return -10
        
        return 10
    
    def value_of_C(self, s: str, i: int, final_index: int) -> int:
        ''' (Solution, str, int, int) -> int
        
        If C comes before a D or a M, return -100. Otherwise, return 100.
        
        >>> soln = Solution()
        >>> soln.value_of_C("CC", 0, 1)
        100
        >>> soln.value_of_I("MCMXCIV", 1, 6)
        -100
        '''
        
        # Check if this C comes before a D or a M
        if i < final_index and s[i+1] in ['D', 'M']:
            return -100
        
        return 100
