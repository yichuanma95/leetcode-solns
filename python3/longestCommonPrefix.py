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
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix: str = strs[0]
        
        for i in range(1, len(strs)):
            letrs: int = 0
            for j in range(min(len(prefix), len(strs[i]))):
                if prefix[j] != strs[i][j]:
                    break
                letrs += 1
            prefix = prefix[:letrs]
            
        return prefix
