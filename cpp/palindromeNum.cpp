/*
Problem 9: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the
same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it
is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string? (Yes, I did)
*/

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        long x_reversed = reverseNum(x);
        return x == x_reversed;
    }
    
private:
    long reverseNum(int x) {
        long reversed = 0;
        while (x > 0) {
            reversed += (x % 10);
            x /= 10;
            reversed *= 10;
        }
        return reversed / 10;
    }
};
