'''
Problem 58: Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return
the length of last word (last word means the last appearing word if we loop from left to right)
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ''' (Solution, str) -> int
        
        Return the length of the last word in a string.
        
        >>> soln = Solution()
        >>> soln.lengthOfLastWord("Hello World")
        5
        '''
        
        # Get all words with at least 1 letter
        words = list(filter(lambda w: len(w) > 0, s.split(" ")))
        
        return 0 if len(words) == 0 else len(words[-1])
