'''
Problem 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        out = []
        
        for i in range(len(nums)):
            if nums[i] in indexDict:
                indexDict[nums[i]].append(i)
            else:
                indexDict[nums[i]] = [i]
        while len(indexDict) > 0:
            num, indices = indexDict.popitem()
            ind = indices.pop(0)
            if len(indices) > 0:
                indexDict[num] = indices
            if (target - num) in indexDict:
                # found the second number
                out.append(ind)
                ind2 = indexDict[target - num][0]
                out.append(ind2)
                out.sort()
                break
        
        return out
