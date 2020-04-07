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
Explanation: You could delete the character 'c'.

Note: The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.checkPalindromeWithSingleDelete(s, True) or self.checkPalindromeWithSingleDelete(s, False)
    
    def checkPalindromeWithSingleDelete(self, s: str, deleteRight: bool) -> bool:
        a = 0
        b = len(s) - 1
        deleted = False
        
        while b > a:
            if s[a] == s[b]:
                a += 1
                b -= 1
            else:
                if deleted:
                    return False
                else:
                    if deleteRight:
                        b -= 1
                    else:
                        a += 1
                    deleted = True
        
        return True
