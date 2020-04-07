'''
Problem 167. Two Sum II-Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that
they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the
target, where index1 must be less than index2.

Note: Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same
element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        
        for i in range(len(numbers)):
            ind2 = self.binSearch(numbers, target - numbers[i], i + 1, len(numbers) - 1)
            if ind2 > 0:
                out.append(i + 1)
                out.append(ind2 + 1)
                break
        
        return out
    
    # because we can assume the list is sorted
    def binSearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right: # target not found in array
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target: # search to the left
            return self.binSearch(nums, target, left, mid - 1)
        else: # search to the right
            return self.binSearch(nums, target, mid + 1, right)
