'''
Problem 35: Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums) - 1)
    
    # returns the index of target in nums
    def binSearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return l
        
        mid: int = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # search right
            return self.binSearch(nums, target, mid + 1, r)
        else:
            # search left
            return self.binSearch(nums, target, l, mid - 1)
