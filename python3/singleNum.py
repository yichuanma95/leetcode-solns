'''
Problem 136: Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find
that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using
extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
* 1 <= nums.length <= 3 * 104
* -3 * 104 <= nums[i] <= 3 * 104
* Each element in the array appears twice except for one element which appears only once.

Solution runtime: 84ms, faster than 96.93% of Python3 submissions
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' (Solution, list of int) -> int
        
        Returns the number that occurs only once in nums, where each other number
        appears twice.
        
        >>> soln = Solution()
        >>> soln.singleNumber([2, 2, 1])
        1
        >>> soln.singleNumber([4, 1, 2, 1, 2])
        4
        '''
        
        # This set will help to find the single number in nums.
        num_set = set()
        
        # For each number in nums, if the number appears for the first time, put it in the
        # set. Otherwise, remove it from the set.
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        
        # At this point, the single number will still be in the set.
        return list(num_set)[0]
