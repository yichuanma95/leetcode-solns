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

class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicates = set()
        uniques = dict()
        
        for i in range(len(s)):
            if s[i] in uniques:
                del uniques[s[i]]
                duplicates.add(s[i])
            else:
                if s[i] not in duplicates:
                    uniques[s[i]] = i

        if len(uniques) == 0:
            return -1
        return min(uniques.values())
