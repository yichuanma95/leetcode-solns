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
        l: int = 0
        r: int = len(s) - 1
        s = s.lower()
        
        while r >= l:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
