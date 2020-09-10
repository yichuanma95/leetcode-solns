'''
Problem 345: Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note: The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ['a','e','i','o','u','A','E','I','O','U']
        letters = list(s)
        extracted_vowels = ""
        for i, letter in enumerate(letters):
            if letter in vowel_list:
                extracted_vowels += letter
                letters[i] = '_'
        extracted_vowels = self.reverse_string(extracted_vowels)
        j = 0
        for i, letter in enumerate(letters):
            if letter == '_':
                letters[i] = extracted_vowels[j]
                j += 1
        return ''.join(letters)
    
    def reverse_string(self, s):
        return s[::-1]
