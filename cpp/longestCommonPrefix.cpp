/*
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
*/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0)
            return "";
        int minLen = strs[0].length();
        for (int i = 1; i < strs.size(); i++) {
            minLen = min(minLen, (int) strs[i].length());
        }
        string prefix = "";
        for (int i = 0; i < minLen; i++) {
            if (!isCommonChar(strs, i))
                break;
            prefix += strs[0][i];
        }
        return prefix;
    }

private:
    bool isCommonChar(vector<string>& strs, int i) {
        for (int j = 0; j < strs.size() - 1; j++) {
            string currentStr = strs[j];
            string nextStr = strs[j+1];
            if (currentStr[i] != nextStr[i])
                return false;
        }
        return true;
    }
};
