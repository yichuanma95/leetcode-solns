'''
Problem 409: Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the
longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here. 

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2

Constraints:
* 1 <= s.length <= 2000
* s consits of lower-case and/or upper-case English letters only.

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_frequencies = defaultdict(int)
        for c in s:
            letter_frequencies[c] += 1
        evens = sum(filter(lambda x: x % 2 == 0, letter_frequencies.values()))
        odds = list(filter(lambda x: x % 2 != 0, letter_frequencies.values()))
        return evens + (sum(odds) - (len(odds) - 1) if len(odds) > 0 else 0)
    