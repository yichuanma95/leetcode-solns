'''
Problem 242: Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note: You may assume the string contains only lowercase alphabets.

Follow up: What if the inputs contain unicode characters? How would you adapt your solution to
such a case?

Solution runtime: 40ms, faster than 91.26% of Python3 submissions

Solution memory usage: 13.1 MB, less than 100% of Python3 submissions
'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        for c in t:
            char_dict[c] -= 1
        return len(list(filter(lambda x: x != 0, char_dict.values()))) == 0
