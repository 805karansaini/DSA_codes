# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freqBucket = [[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freqBucket[count].append(num)
        res = []
        for i in range(len(freqBucket) - 1, 0, -1):
            for num in freqBucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # dic = defaultdict(int)
        # for num in nums:
        #     dic[num] += 1
        # # res = []
        # dic = dict(sorted(dic.items(), key=lambda item: item[1],  reverse=True))
        # i = 0
        # for key,val in dic.items():
        #     if i < k:
        #         res.append(key)
        #         i += 1
        # return res
