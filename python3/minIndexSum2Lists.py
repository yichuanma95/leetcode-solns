'''
Problem 599: Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of
favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is 
a choice tie between answers, output all of them with no order requirement. You could assume
there always exists an answer.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum
1 (0+1).

Example 3:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:
Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]

Constraints:
* 1 <= list1.length, list2.length <= 1000
* 1 <= list1[i].length, list2[i].length <= 30
* list1[i] and list2[i] consist of spaces ' ' and English letters.
* All the stings of list1 are unique.
* All the stings of list2 are unique.

Solution runtime: 148ms, faster than 97.26% of Python3 submissions

Solution memory usage: 12.9 MB, less than 100% of Python3 submissions
'''

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        andy_indices = {}
        for i, resto in enumerate(list1):
            andy_indices[resto] = i
        min_index_sum = len(list1) + len(list2) + 1
        doris_indices = {}
        for i, resto in enumerate(list2):
            if resto in andy_indices:
                min_index_sum = min(min_index_sum, i + andy_indices[resto])
                doris_indices[resto] = i
        common = []
        for resto, i in doris_indices.items():
            if i + andy_indices[resto] == min_index_sum:
                common.append(resto)
        return common
