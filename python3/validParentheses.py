'''
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
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack : List[str] = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for b in s:
            if b in ['(', '{', '[']:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                if brackets[b] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
