'''
Problem 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note: All given inputs are in lowercase letters a-z.

Solution runtime: 28ms, faster than 90.21% of Python3 submissions
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ''' (Solution, list of str) -> str
        
        Return the longest common prefix among the strings in strs.
        
        >>> soln = Solution()
        >>> soln.longestCommonPrefix(["flower", "flow", "flight"])
        "fl"
        >>> soln.longestCommonPrefix(["dog", "racecar", "car"])
        ""
        '''
        
        if len(strs) == 0:
            return ''
        
        # Get the minimal string length of all strings in str
        min_len = min([len(s) for s in strs])
        prefix = ''
        
        # For each index in the minimal length, check if the character at that index in each
        # of the strings is the same. If not, the longest common prefix has been
        # found. Otherwise, add it to the prefix.
        for i in range(min_len):
            if not self.is_common_char(strs, i):
                break
            prefix += strs[0][i]
        
        return prefix

    def is_common_char(self, strs: List[str], i: int) -> bool:
        ''' (Solution, list of str, int) -> bool
        
        Return True iff the character at index i is the same for all strings in strs.
        
        >>> soln = Solution()
        >>> soln.is_common_char(["flower", "flow", "flight"], 0)
        True
        >>> soln.is_common_char(["dog", "racecar", "car"], 0)
        False
        '''
        
        num_strs = len(strs)
        
        # Check if the character at index i is the same for all strings in strs
        for j in range(num_strs - 1):
            current_str = strs[j]
            next_str = strs[j+1]
            if current_str[i] != next_str[i]:
                return False
        
        return True
    