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

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letter_count = self.get_letter_count(ransomNote)
        mag_letter_count = self.get_letter_count(magazine)
        for key in note_letter_count.keys():
            if note_letter_count[key] > mag_letter_count[key]:
                return False
        return True
    
    def get_letter_count(self, text):
        letter_count = defaultdict(int)
        for c in text:
            letter_count[c] += 1
        return letter_count
