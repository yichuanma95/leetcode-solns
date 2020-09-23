'''
Problem 500: Keyboard Row

Given a List of words, return the words that can be typed using letters of the alphabet on only
one row of the American keyboard.

*image of the American keyboard on LeetCode*
 
Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Notes:
1. You may use one character in the keyboard more than once.
2. You may assume the input string will only contain letters of alphabet.
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            searchable_word = set(word.lower())
            if self.is_word_in_row(searchable_word):
                result.append(word)
        return result
    
    def is_word_in_row(self, word):
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for row in rows:
            all_letters = len(row)
            no_letters = len(row) + len(word)
            combined = row.union(word)
            if len(combined) > all_letters and len(combined) < no_letters:
                return False
            if len(combined) == all_letters:
                return True
