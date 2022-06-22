# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time Complexity is O(nlogk)  where log k is insertion of element in heap
        # by default in python we get heap as min heap to get max heap we can push -x
        h = []
        def push(x):
            heapq.heappush(h, x)
        def pop():
            return heapq.heappop(h)
        
        for n in nums:
            push(n)
            if len(h) > k:
                pop()
        return pop()
        
#         time Complexity is O(nlogn) bad
#         nums.sort()
#         return nums[-k]