/*
Problem 58: Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return
the length of last word (last word means the last appearing word if we loop from left to right)
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5

Solution runtime: 4ms, faster than 91.93% of C++ submissions
*/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0, currentCharIndex = s.length() - 1;
        while (s[currentCharIndex] == ' ') {
            currentCharIndex--;
        }
        for (int i = currentCharIndex; i >= 0; i--) {
            if (s[i] == ' ') break;
            len++;
        }
        return len;
    }
};
