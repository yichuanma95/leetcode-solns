'''
Problem 283: Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Notes:
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

Solution memory usage: 13.9 MB, less than 100% of Python3 submissions
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        for p2 in range(len(nums)):
            p1 = self.move_zero_and_adjust_p1(nums, p1, p2)
    
    def move_zero_and_adjust_p1(self, nums, p1, p2):
        if nums[p1] != 0:
            return p1 + 1
        if nums[p1] == 0 and nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            return p1 + 1
        return p1
