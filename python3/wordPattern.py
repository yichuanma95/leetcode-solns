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
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        num_words = len(words)
        if num_words != len(pattern):
            return False
        letter_to_word = {}
        word_to_letter = {}
        for i in range(num_words):
            if words[i] in word_to_letter and word_to_letter[words[i]] != pattern[i]:
                return False
            if pattern[i] in letter_to_word and letter_to_word[pattern[i]] != words[i]:
                return False
            letter_to_word[pattern[i]] = words[i]
            word_to_letter[words[i]] = pattern[i]
        return True
