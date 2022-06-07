# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m < 1:
            i = 0
            while i < n:
                nums1[i] = nums2[i]
                i += 1
            return

        if n < 1:
            return

        i = len(nums1) - 1
        while m and n:
            # print(m, " m : n", n)
            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                i -= 1
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
                i -= 1

        while n:
            # print("n" , n)
            nums1[i] = nums2[n - 1]
            n -= 1
            i -= 1
        while m:
            # print("n" , m)
            nums1[i] = nums1[m - 1]
            i -= 1
            m -= 1

        return
