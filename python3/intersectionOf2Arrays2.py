'''
Problem 350: Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
-Each element in the result should appear as many times as it shows in both arrays.
-The result can be in any order.

Follow up:
-What if the given array is already sorted? How would you optimize your algorithm?
-What if nums1's size is small compared to nums2's size? Which algorithm is better?
-What if elements of nums2 are stored on disk, and the memory is limited such that you cannot
 load all elements into the memory at once?

Solution runtime: 40ms, faster than 93.79% of Python3 submissions

Solution memory usage: 12.9 MB, less than 100% of Python3 submissions
'''

import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = collections.defaultdict(int)
        for num in nums1:
            d1[num] += 1
        d2 = collections.defaultdict(int)
        for num in nums2:
            d2[num] += 1
        intersect = []
        
        for key in d1.keys():
            if key in d2:
                for i in range(min(d1[key], d2[key])):
                    intersect.append(key)
        
        return intersect
