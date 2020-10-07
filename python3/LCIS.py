'''
Problem 674: Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence
(subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

Note: Length of the array will not exceed 10,000.

Solution runtime: 72ms, faster than 92.1% of Python3 submissions
'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        LCIS_len = 0
        current_CIS_len = 1 if len(nums) > 0 else 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                LCIS_len = max(LCIS_len, current_CIS_len)
                current_CIS_len = 1
            else:
                current_CIS_len += 1
        return max(LCIS_len, current_CIS_len)
