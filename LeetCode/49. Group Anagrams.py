from collections import Counter
# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]
# Output: [[""]]
# Input: strs = ["a"]
# Output: [["a"]]
# time Complexity (m*n*26)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            dic[tuple(count)].append(s)

        return dic.values()

# won work timecomplexity is high
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     res = []
#     count = []
#     for word in strs:
#         c = Counter(word)
#         for i, cnt in enumerate(count):
#             if c == cnt:
#                 res[i].append(word)
#                 break
#         else:
#             count.append(c)
#             res.append([word])
#     return res
#
# ans = groupAnagrams(strs)
# print(ans)
