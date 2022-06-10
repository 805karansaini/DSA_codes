# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        # c1 = Counter(s)
        # c2 = Counter(t)
        # if c1 == c2:
        #     return True
        # return False