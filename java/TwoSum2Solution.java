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

Solution memory usage: 39.2 MB, less than 90.47% of Java submissions
*/

class TwoSum2Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Set up a hash map to store numbers and their respective indices in numbers.
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        // Loop through numbers to find a pair of indices that refer to the numbers in
        // numbers that add up to target.
        int length = numbers.length;
        for (int i = 0; i < length; i++) {
            int num = numbers[i], complement = target - num;
            
            // If the complement, that is the difference between the current number and
            // target is in numToIndex, a solution has been found.
            if (numToIndex.containsKey(complement)) {
                int[] result = {numToIndex.get(complement) + 1, i + 1};
                Arrays.sort(result);
                return result;
            }
            
            // Otherwise, add the current number and its index to numToIndex.
            numToIndex.put(num, i);
        }
        
        // Return something to get this code to compile.
        return new int[2];
    }
}
