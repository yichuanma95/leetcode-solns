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
'''

class Solution(object):
    def rob(self, nums):
        ''' (Solution, list of int) -> int
        
        Returns the maximum amount of money stashed in non-adjacent houses in a
        community represented by the given list nums, where each element in nums is a
        house with a certain amount of money stashed in it.
        
        >>> soln = Solution()
        >>> soln.rob([1, 2, 3, 1])
        4
        >>> soln.rob([2, 7, 9, 3, 1])
        12
        '''
        
        n = len(nums)
        # Base cases:
        # nums.length = 0
        if n == 0:
            return 0
        
        # nums.length < 3
        if n < 3:
            return max(nums)
        
        # This list contains the maximum amount that can be robbed after the robber robs
        # the ith house for i <= n.
        theft_amounts = [nums[0], nums[1], nums[0] + nums[2]]
        
        # Induction formula: theft_amounts[i] = nums[i] + max(theft_amounts[i-2], theft_amounts[i-3])
        for i in range(3, n):
            theft_amounts.append(nums[i] + max(theft_amounts[i-2], theft_amounts[i-3]))
            
        # Return the max amount in the theft amounts list
        return max(theft_amounts)
    