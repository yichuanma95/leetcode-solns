'''
Problem 680: Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it
a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c' or 'b' to make s a palindrome.

Note: The string will only contain lowercase characters a-z. The maximum length of the string
is 50000.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.check_if_palindrome(s, left + 1, right) or \
                    self.check_if_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def check_if_palindrome(self, s, left, right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
