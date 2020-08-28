/*
Problem 326: Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up: Could you do it without using any loop / recursion?

Solution runtime: 252ms, faster than 91.67% of TypeScript submissions
*/

function isPowerOfThree(n: number): boolean {
    return n > 0 && Math.pow(3, Math.round(Math.log(n) / Math.log(3))) == n;
};
