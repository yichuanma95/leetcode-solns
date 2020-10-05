'''
Problem 643: Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that
has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Notes:
1. 1 <= k <= n <= 30,000.
2. Elements of the given array will be in the range [-10,000, 10,000].

Solution runtime: 792ms, faster than 98.24% of Python3 submissions
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = sum(nums[:k])
        current = best
        for i in range(len(nums) - k):
            current += (nums[i+k] - nums[i])
            best = max(best, current)
        return best / k
