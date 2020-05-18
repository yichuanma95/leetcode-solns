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
        ''' (Solution, str) -> bool
        
        Return True iff a string of brackets '()', '{}', or '[]' has all open brackets
        closed by the same type of brackets and in the correct order.
        
        >>> soln = Solution()
        >>> soln.isValid("()")
        True
        >>> soln.isValid("()[]{}")
        True
        >>> soln.isValid("(]")
        False
        >>> soln.isValid("([)]")
        False
        >>> soln.isValid("{[]}")
        True
        '''
        
        # Set up a dictionary that stores right brackets and their corresponding left
        # brackets, along with a stack to store the open brackets read so far.
        right_to_left = {'}': '{', ')': '(', ']': '['}
        bracket_stack = []
        left_brackets = {'{', '[', '('}
        
        # For each character in s, if it's a left bracket, push it to the stack.
        # Otherwise, determine if it matches the bracket on top of the stack.
        for c in s:
            if c in left_brackets:
                bracket_stack.append(c)
            else:
                if len(bracket_stack) == 0 or right_to_left[c] != bracket_stack[-1]:
                    return False
                bracket_stack.pop()
        
        return len(bracket_stack) == 0
