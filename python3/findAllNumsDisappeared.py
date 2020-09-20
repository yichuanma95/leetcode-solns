'''
Problem 448: Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice
and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does
not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counters = [0] * (len(nums) + 1)
        for num in nums: 
            counters[num] += 1
        result = []
        for n, c in enumerate(counters):
            if n == 0:
                continue
            if c == 0:
                result.append(n)
        return result
