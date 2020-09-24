'''
Problem 506: Relative Ranks

Given scores of N athletes, find their relative ranks and the people with the top three
highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold
Medal", "Silver Medal" and "Bronze Medal". 
For the remaining two athletes, you just need to output their relative ranks according to
their scores.

Notes:
1. N is a positive integer and won't exceed 10,000.
2. All the scores of athletes are guaranteed to be unique.
'''

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_nums = sorted(nums, reverse=True)
        score_to_rank = {}
        if len(nums) >= 1:
            score_to_rank[sorted_nums[0]] = "Gold Medal"
        if len(nums) >= 2:
            score_to_rank[sorted_nums[1]] = "Silver Medal"
        if len(nums) >= 3:
            score_to_rank[sorted_nums[2]] = "Bronze Medal"
        for i in range(3, len(nums)):
            score_to_rank[sorted_nums[i]] = str(i + 1)
        return list(map(lambda x: score_to_rank[x], nums))
