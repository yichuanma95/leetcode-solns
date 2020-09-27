/*
'''
Problem 53: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which\
has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up: If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.

Solution runtime: 8ms, faster than 97.3% of C++ submissions
*/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> maxSums;
        maxSums.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            maxSums.push_back(max(maxSums[i-1] + nums[i], nums[i]));
        }
        return *max_element(maxSums.begin(), maxSums.end());
    }
};
