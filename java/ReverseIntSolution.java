/*
Problem 7: Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.
*/

class ReverseIntSolution {
    public int reverse(int x) {
        boolean isNegative = x < 0;
        long reversedNum = reverseNum(Math.abs(x));
        
        if (reversedNum > (long)Integer.MAX_VALUE || reversedNum < (long)Integer.MIN_VALUE)
            return 0;
        
        return isNegative ? (int)(-reversedNum) : (int)reversedNum;
    }
    
    private long reverseNum(int x) {
        long reversed = 0;
        
        while (x > 0) {
            reversed += (x % 10);
            x /= 10;
            reversed *= 10;
        }
        
        // Because reversed was multiplied by 10 ine extra time in the loop, reversed should
        // be divided by 10 before being returned.
        return reversed / 10;
    }
}
