'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a *subsequence* and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' (Solution, str) -> int
        
        Returns the length of the longest substring in s that does not contain
        repeating characters.
        
        >>> soln = Solution()
        >>> soln.lengthOfLongestSubstring("abcabcbb")
        3
        >>> soln.lengthOfLongestSubstring("bbbbb")
        1
        >>> soln.lengthOfLongestSubstring("pwwkew")
        3
        '''
        
        # This dictionary keeps track of each unique letter in s and the index it last
        # appeared at.
        letter_to_index = {}
        max_length = 0
        
        # This pointer marks the beginning of the current substring without
        # repeating characters in s. It should never move backwards.
        substr_begin = 0
        
        # For each char c in s, if c is in the dict, move the substring beginning
        # pointer forward to the index after the one where c was last at. Put c and
        # the current index into the dict and update the length of the longest substring
        # without repeating chars along the way.
        for i, c in enumerate(s):
            if c in letter_to_index:
                substr_begin = max(letter_to_index[c] + 1, substr_begin)
            letter_to_index[c] = i
            max_length = max(max_length, i + 1 - substr_begin)
        
        return max_length
