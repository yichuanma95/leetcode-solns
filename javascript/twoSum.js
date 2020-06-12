/*
Problem 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let twoSum = (nums, target) => {
    // Set up a dictionary to store numbers and their respective indices in nums.
    let numToIndex = new Map()
    
    // Loop through nums to find a pair of indices that refer to numbers in nums that add up
    // to target.
    let length = nums.length
    for (let i = 0; i < length; i++) {
        let num = nums[i];
        let complement = target - num;
        
        // If the complement, that is the difference between the current number and target,
        // is in numToIndex, a solution has been found.
        if (numToIndex.has(complement))
            return [numToIndex.get(complement), i];
        
        // Otherwise, add the current number and its index to numToIndex.
        numToIndex.set(num, i);
    }
};
