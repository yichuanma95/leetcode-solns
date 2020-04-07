'''
Problem 290: Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and
a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Note: You may assume pattern contains only lowercase letters, and str contains lowercase
letters that may be separated by a single space.

Solution runtime: 28ms, faster than 90.78% of Python3 submissions

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        words: List[str] = string.split(" ")
        if len(pattern) != len(words):
            return False
        
        charMap = {}
        wordMap = {}
        
        for i in range(len(pattern)):
            if pattern[i] in charMap:
                if charMap[pattern[i]] != words[i]:
                    return False
            else:
                charMap[pattern[i]] = words[i]
            if words[i] in wordMap:
                if wordMap[words[i]] != pattern[i]:
                    return False
            else:
                wordMap[words[i]] = pattern[i]
        
        return True
