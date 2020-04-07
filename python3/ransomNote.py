'''
Problem 383: Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the
magazines, write a function that will return true if the ransom note can be constructed from
the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note: You may assume that both strings contain only lowercase letters.

Examples:
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lettersNeeded = collections.defaultdict(int)
        for l in ransomNote:
            lettersNeeded[l] += 1
        lettersAvailable = collections.defaultdict(int)
        for l in magazine:
            lettersAvailable[l] += 1
        
        for key in lettersNeeded.keys():
            if key not in lettersAvailable:
                return False
            if lettersNeeded[key] > lettersAvailable[key]:
                return False
        
        return True
