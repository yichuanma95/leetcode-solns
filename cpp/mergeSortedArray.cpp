/*
Problem 88: Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Notes:
-The number of elements initialized in nums1 and nums2 are m and n respectively.
-You may assume that nums1 has enough space (size that is equal to m + n) to hold
additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Constraints:
* -10^9 <= nums1[i], nums2[i] <= 10^9
* nums1.length == m + n
* nums2.length == n
*/

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums1Only;
        int nums1Index = 0, nums1OnlyIndex = 0, nums2Index = 0;
        for (int i = 0; i < m; i++) {
            nums1Only.push_back(nums1[i]);
        }
        while (nums1OnlyIndex < m && nums2Index < n) {
            if (nums1Only[nums1OnlyIndex] <= nums2[nums2Index]) {
                nums1[nums1Index] = nums1Only[nums1OnlyIndex];
                nums1OnlyIndex++;
            } else {
                nums1[nums1Index] = nums2[nums2Index];
                nums2Index++;
            }
            nums1Index++;
        }
        if (nums1OnlyIndex < m) {
            mergeRemainder(nums1, nums1Index, nums1Only, nums1OnlyIndex);
        } else {
            mergeRemainder(nums1, nums1Index, nums2, nums2Index);
        }
    }
    
private:
    void mergeRemainder(vector<int>& nums1, int nums1Index, vector<int>& nums, int numsIndex) {
        int k = nums.size();
        for (int i = numsIndex; i < k; i++) {
            nums1[nums1Index] = nums[i];
            nums1Index++;
        }
    }
};
