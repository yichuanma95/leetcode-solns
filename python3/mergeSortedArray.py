'''
Problem 88: Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Notes:
-The number of elements initialized in nums1 and nums2 are m and n respectively.
-You may assume that nums1 has enough space (size that is greater or equal to m + n) to
hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_only = nums1[:m]
        nums1_index = 0
        nums1_only_index = 0
        nums2_index = 0
        
        while nums1_only_index < m and nums2_index < n:
            if nums1_only[nums1_only_index] <= nums2[nums2_index]:
                nums1[nums1_index] = nums1_only[nums1_only_index]
                nums1_only_index += 1
            else:
                nums1[nums1_index] = nums2[nums2_index]
                nums2_index += 1
            nums1_index += 1
        
        if nums1_only_index < m:
            self.merge_remainder(nums1, nums1_index, nums1_only, nums1_only_index)
        else:
            self.merge_remainder(nums1, nums1_index, nums2, nums2_index)
    
    def merge_remainder(self, nums1, nums1_index, nums, nums_index):
        k = len(nums)
        
        for i in range(nums_index, k):
            nums1[nums1_index] = nums[i]
            nums1_index += 1
