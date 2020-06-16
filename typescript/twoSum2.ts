/*
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

Solution runtime: 72ms, faster than 100% of TypeScript submissions

Solution memory usage: 36.9 MB, less than 100% of TypeScript submissions
*/

function twoSum(numbers: number[], target: number): number[] {
    // Set up a map to store numbers and their respective indices in nums.
    let numToIndex = new Map()
    
    // Loop through numbers to find a pair of indices that refer to the numbers in numbers
    // that add up to target.
    let length = numbers.length;
    for (let i = 0; i < length; i++) {
        let num = numbers[i];
        let complement = target - num;
        
        // If the complement, that is the difference between the current number and target,
        // is in numToIndex, a solution has been found.
        if (numToIndex.has(complement)) {
            let result = [numToIndex.get(complement) + 1, i + 1];
            result.sort((a, b) => a - b);
            return result;
        }
        
        
        // Otherwise, add the current number and its index to numToIndex.
        numToIndex.set(num, i);
    }
    
    // Return something to get this code to compile.
    return [0];
};
