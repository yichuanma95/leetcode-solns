'''
Problem 389: Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a
random position.

Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letters = self.get_letter_frequencies(s)
        t_letters = self.get_letter_frequencies(t)
        for k, v in t_letters.items():
            if v - s_letters[k] == 1:
                return k
    
    def get_letter_frequencies(self, s):
        letters = defaultdict(int)
        for c in s:
            letters[c] += 1
        return letters
