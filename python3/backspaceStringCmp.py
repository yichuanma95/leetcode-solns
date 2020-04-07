'''
Problem 844: Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text
editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Notes:
1. 1 <= S.length <= 200
2. 1 <= T.length <= 200
3. S and T only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(N) time and O(1) space?

Solution runtime: 32ms, faster than 95.03% of Python3 submissions
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        
        for i in range(len(S)):
            if S[i] == '#':
                try:
                    stackS.pop()
                except IndexError:
                    pass
            else:
                stackS.append(S[i])
        for i in range(len(T)):
            if T[i] == '#':
                try:
                    stackT.pop()
                except IndexError:
                    pass
            else:
                stackT.append(T[i])
        newS = ''.join(stackS)
        newT = ''.join(stackT)
        
        return newS == newT
