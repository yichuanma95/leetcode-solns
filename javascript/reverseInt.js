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

/**
 * @param {number} x
 * @return {number}
 */
let reverse = x => {
    let isNegative = x < 0;
    let reversedNum = reverseNum(Math.abs(x));
    let maxInt = Math.pow(2, 31);
    
    if (-reversedNum < -maxInt || reversedNum > maxInt - 1)
        return 0
    
    return isNegative ? -reversedNum : reversedNum;
};

/**
 * @param {number} x
 * @return {number}
 */
let reverseNum = x => {
    let reversed = 0;
    
    while (x > 0) {
        reversed += (x % 10);
        x = (x / 10) >> 0;
        reversed *= 10;
    }
    
    // Because reversed was multiplied by 10 one extra time in the while loop, reversed
    // should be integer-divided by 10 before being returned.
    return reversed / 10;
};
