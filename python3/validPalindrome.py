'''
Problem 125: Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' (Solution, str) -> bool
        
        Returns True iff the given string is a palindrome. Only alphanumeric characters
        are considered and cases are ignored.
        
        >>> soln = Solution()
        >>> soln.isPalindrome("A man, a plan, a canal: Panama")
        True
        >>> soln.isPalindrome("race a car")
        False
        '''
        
        # Extract all letters and digits from s.
        s = self.extract_alnum_lower(s)
        
        # s[i] and s[j] are the next pair of characters to compare
        i = 0
        j = len(s) - 1

        # The characters in s[:i] have been successfully compared to those in s[j:].
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        # If we exited because we successfully compared all pairs of characters, then j <= i.
        return j <= i
        
    def extract_alnum_lower(self, s):
        ''' (Solution, str) -> str
        
        Returns a new string containing only the alphanumeric characters in the given
        string. The alphabetic characters in the returned string are all lower-case.
        
        >>> soln = Solution()
        >>> soln.extract_alnum_lower("A man, a plan, a canal: Panama")
        "amanaplanacanalpanama"
        >>> soln.extract_alnum_lower("race a car")
        "raceacar"
        '''
        
        return ''.join(list(filter(lambda c: c.isalnum(), s))).lower()
