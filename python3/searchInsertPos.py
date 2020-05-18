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
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            middle = (low + high) // 2
            
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        
        return low
    