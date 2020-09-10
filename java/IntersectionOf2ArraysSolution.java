/*
Problem 349: Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Notes:
-Each element in the result must be unique.
-The result can be in any order.

Solution runtime: 2ms, faster than 99.46% of Java submissions
*/

class IntersectionOf2ArraysSolution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = createSet(nums1);
        Set<Integer> set2 = createSet(nums2);
        set1.retainAll(set2);
        int[] result = new int[set1.size()];
        int i = 0;
        for (int num: set1) {
            result[i++] = num;
        }
        return result;
    }
    
    private Set<Integer> createSet(int[] nums) {
        Set<Integer> intSet = new HashSet();
        for (int num: nums) {
            intSet.add(num);
        }
        return intSet;
    }
}
