/*
Problem 20: Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
*/

class Solution {
public:
    bool isValid(string s) {
        vector<char> bracketStack;
        map<char, char> rightToLeft = {
            {'}', '{'},
            {']', '['},
            {')', '('}
        };
        set<char> leftBrackets;
        leftBrackets.insert('{');
        leftBrackets.insert('[');
        leftBrackets.insert('(');
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (leftBrackets.find(c) != leftBrackets.end()) {
                bracketStack.push_back(c);
            } else {
                if (bracketStack.size() == 0 || rightToLeft[c] != bracketStack.back())
                    return false;
                bracketStack.pop_back();
            }
        }
        return bracketStack.size() == 0;
    }
};
