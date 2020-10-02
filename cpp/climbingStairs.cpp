/*
Problem 70: Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
* 1 <= n <= 45

Solution runtime: 0ms, faster than 100% of C++ submissions
*/

class Solution {
public:
    int climbStairs(int n) {
        double sqrt5 = sqrt(5.0);
        double phi = (1.0 + sqrt5) / 2;
        double psi = (1.0 - sqrt5) / 2;
        return (int)((pow(phi, n + 1.0) - pow(psi, n + 1.0)) / sqrt5);
    }
};
