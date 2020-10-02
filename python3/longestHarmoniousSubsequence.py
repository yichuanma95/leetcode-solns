'''
Problem 594: Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value and
its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all
its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or
no elements without changing the order of the remaining elements. 

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

Constraints:
* 1 <= nums.length <= 2 * 104
* -109 <= nums[i] <= 109

Solution runtime: 312ms, faster than 93.42% of Python3 submissions
'''

from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_freq = Counter(nums)
        if len(num_freq) == 1:
            return 0
        sorted_items = sorted(num_freq.items(), key=lambda x: x[1], reverse=True)
        result = 0
        max_result = 0
        for num, freq in sorted_items:
            if num - 1 not in num_freq and num + 1 not in num_freq:
                continue
            result = freq
            minus_flag = False
            if num - 1 in num_freq:
                minus_flag = True
                temp = num_freq[num-1]
            if num + 1 in num_freq:
                temp = max(num_freq[num-1], num_freq[num+1]) if minus_flag else num_freq[num+1]
            result += temp
            max_result = max(max_result, result)
        return max_result
