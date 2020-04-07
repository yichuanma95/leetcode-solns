'''
Problem 409: Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note: Assume the length of given string will not exceed 1,010.

Example:
Input: "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        letters = collections.defaultdict(int)
        evens = 0
        odds = 0
        hasOdd = False
        
        for c in s:
            letters[c] += 1
        for val in letters.values():
            if val % 2 == 0:
                evens += val
            else:
                odds += (val - 1)
                hasOdd = True
        
        if hasOdd:
            return evens + odds + 1
        else:
            return evens
        