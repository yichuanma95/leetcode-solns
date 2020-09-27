'''
Problem 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order. 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] 

Constraints:
* 2 <= nums.length <= 105
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.
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
