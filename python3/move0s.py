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
        pointer2 = 0
        
        for i in range(1, len(nums)):
            if nums[pointer2] == 0:
                if nums[i] != 0:
                    nums[i], nums[pointer2] = nums[pointer2], nums[i]
                    pointer2 += 1
            else:
                pointer2 += 1
