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

Solution memory usage: 5.1 MB, less than 92.31% of C submissions
*/

bool isPowerOfTwo(int n){
    while (!(n & 1) && n)
        n >>= 1;
    
    return n == 1;
}
