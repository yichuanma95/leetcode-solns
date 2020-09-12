'''
Problem 414: Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does
not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))
        first_max = max(nums)
        if len(distinct_nums) < 3:
            return first_max
        second_max = min(nums)
        for num in distinct_nums:
            if num > second_max and num < first_max:
                second_max = num
        third_max = min(nums)
        for num in distinct_nums:
            if num > third_max and num < second_max:
                third_max = num
        return third_max
