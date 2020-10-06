'''
Problem 665: Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing
by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
* 1 <= n <= 10 ^ 4
* - 10 ^ 5 <= nums[i] <= 10 ^ 5

Solution runtime: 156ms, faster than 100% of Python3 submissions
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1] and p >= 0:
                return False
            if nums[i] > nums[i+1]:
                p = i

        return p <= 0 or p == len(nums) - 2 or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]
