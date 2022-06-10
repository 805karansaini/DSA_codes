# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        dic = defaultdict(int)
        best = 0
        while fast < len(s):
            if s[fast] in dic:
                best = max(best, fast - slow)
                while slow < fast:
                    if s[slow] == s[fast]:
                        del dic[s[slow]]
                        dic[s[fast]] = fast
                        slow += 1
                        break
                    else:
                        del dic[s[slow]]
                        slow += 1
            else:
                dic[s[fast]] = fast
            fast += 1

        best = max(best, fast - slow)
        return best

def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    left, res = 0, 0
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        res = max(res, right-left + 1)
    return res