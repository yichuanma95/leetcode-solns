import java.util.Map;
import java.util.HashMap;

/*
Problem 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution runtime: 1ms, faster than 99.93% of Java submissions
*/

class TwoSumSolution {
    public int[] twoSum(int[] nums, int target) {
        // Set up a hash map to store numbers and their respective indices in nums.
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        // Loop through nums to find a pair of indices that refer to numbers in nums that
        // add up to target.
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            int num = nums[i];
            int complement = target - num;
            
            // If the complement, that is difference between the current number and target,
            // is in numToIndex, a solution has been found.
            if (numToIndex.containsKey(complement)) {
                int[] result = {numToIndex.get(complement), i};
                return result;
            }
            
            // Otherwise, add the current number and its index to numToIndex.
            numToIndex.put(num, i);
        }
        
        return new int[2];
    }
}
