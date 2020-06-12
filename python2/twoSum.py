'''
Problem 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution rumtime: 32ms, faster than 94.27% of Python submissions.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' (Solution, list of ints, int) -> list of ints
        
        Return the indices of two numbers in the given list such that those two numbers in
        the list add up to the given target.
        
        >>> soln = Solution()
        >>> soln.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        '''
        
        # Set up a dictionary to store numbers and their respective indices in nums.
        num_to_index = {}
        
        # Loop through nums to find a pair of indices that refer to numbers in nums that add
        # up to target.
        length = len(nums)
        for i in range(length):
            num = nums[i]
            diff_from_target = target - num
            
            # If the difference between the current number and target is in num_to_index,
            # a solution has been found.
            if diff_from_target in num_to_index:
                return [num_to_index[diff_from_target], i]
            
            # Otherwise, add the current number and its index to num_to_index.
            num_to_index[num] = i
