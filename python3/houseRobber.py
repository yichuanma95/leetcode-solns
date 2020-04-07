'''
Problem 198: House Robber

You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of them is
that adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Solution runtime: 24ms, faster than 96.92% of Python3 submissions

Solution memory usage: 12.7 MB, less than 100% of Python3 submissions
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        C = [nums[0], nums[1], nums[0] + nums[2]]
        
        for i in range(3, len(nums)):
            C.append(max(C[-1], C[-2] + nums[i], C[-3] + nums[i]))
        
        return C[-1]
