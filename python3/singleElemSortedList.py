'''
Problem 540: Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears exactly twice except
for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return self.customBinSearch(nums, 0, len(nums) - 1)

    def customBinSearch(self, nums: List[int], l: int, r: int) -> int:
        if l > r:
            return -1
        
        mid: int = (l + r) // 2
        
        if mid == 0 or mid == len(nums) - 1:
            return nums[mid]
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if mid % 2 != 0: # mid is odd
            if nums[mid] == nums[mid - 1]: # duplicate is to the left
                return self.customBinSearch(nums, mid + 1, r) # search right
            else:
                return self.customBinSearch(nums, l, mid - 1) # search left
        else: # mid is even
            if nums[mid] == nums[mid + 1]: # duplicate is to the right
                return self.customBinSearch(nums, mid, r) # search right
            else:
                return self.customBinSearch(nums, l, mid) # search left
