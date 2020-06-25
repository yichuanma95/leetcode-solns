'''
Problem 205: Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character but a character may map
to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note: You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        ''' (Solution, str, str) -> bool
        
        Precondition: s and t must have the same length.
        
        Returns True iff s and t are isomorphic; that is, each char in s can be replaced to
        get t.
        
        >>> soln = Solution()
        >>> soln.isIsomorphic('egg', 'add')
        True
        >>> soln.isIsomorphic('foo', 'bar')
        False
        >>> soln.isIsomorphic('paper', 'title')
        True
        '''
        
        # This dictionary maps each char in s to the corresponding char in t.
        s_to_t = {}
        
        # This dictionary maps each char in t to the corresponding char in s.
        t_to_s = {}
        
        str_len = len(s)
        for i in range(str_len):
            s_char = s[i]
            t_char = t[i]
            
            # If the value for the current char in s in s_to_t is different from the
            # current char in t, s and t are not isomorphic.
            s_value = s_to_t.setdefault(s_char, t_char)
            if s_value != t_char:
                return False
            
            # If the value for the current char in t in t_to_s is different from the
            # current char in s, s and t are not isomorphic.
            t_value = t_to_s.setdefault(t_char, s_char)
            if t_value != s_char:
                return False
        
        return True
