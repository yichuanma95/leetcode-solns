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

Memory usage: 13.1 MB, less than 100% of Python3 submissions
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersOfS = {}
        for c in s:
            if c in lettersOfS:
                lettersOfS[c] += 1
            else:
                lettersOfS[c] = 1
        lettersOfT = {}
        for c in t:
            if c in lettersOfT:
                lettersOfT[c] += 1
            else:
                lettersOfT[c] = 1
        
        return lettersOfS == lettersOfT
