/*
Problem 231: Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false

Solution memory usage: 38.2 MB, less than 100% of TypeScript submissions
*/

function isPowerOfTwo(n: number): boolean {
    return n > 0 && !(n & (n - 1));
};
