'''
Problem 451: Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input: "tree"
Output: "eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: "cccaaa"
Output: "cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: "Aabb"
Output: "bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequencies = defaultdict(int)
        for c in s:
            char_frequencies[c] += 1
        sorted_list = sorted(char_frequencies.items(), key=lambda x: x[1], reverse=True)
        result_str = ""
        for c, f in sorted_list:
            result_str += (c * f)
        return result_str
    