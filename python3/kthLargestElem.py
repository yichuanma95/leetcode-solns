'''
Problem 215: Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in
the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import heapq

class Solution:
    def findKthLargest_naive(self, nums: List[int], k: int) -> int:
        # Naïve solution using sorting
        nums.sort()
        return nums[-k]

    def findKthLargest_maxheap(self, nums: List[int], k: int) -> int:
        # Faster solution using maxheap
        heap = list(map(lambda x: x * -1, nums))
        heapq.heapify(heap)
        extracted = 0
        for i in range(k):
            extracted = heapq.heappop(heap)
        return extracted * -1
    
    def findKthLargest_minheap(self, nums: List[int], k: int) -> int:
        # Another solution using minheap
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
    