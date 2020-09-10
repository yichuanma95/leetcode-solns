'''
Problem 387: First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it
doesn't exist, return -1.

Examples:
s = "leetcode"
return 0

s = "loveleetcode",
return 2

Note: You may assume the string contain only lowercase letters.

Solution memory usage: 12.9 MB, less than 100% of Python3 submissions
'''

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_to_indices = defaultdict(list)
        for i, c in enumerate(s):
            letters_to_indices[c].append(i)
        indices_of_single_chars = []
        for v in letters_to_indices.values():
            if len(v) == 1:
                indices_of_single_chars.append(v[0])
        return min(indices_of_single_chars) if len(indices_of_single_chars) > 0 else -1
    