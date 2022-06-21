# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# sliding window technique

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N  = len(s)
        best = 10**20
        low, high = 0, 0
        res_high, res_low = 0, 0
        
        dic = defaultdict(int)
        for c in t:
            dic[c] += 1
        count = len(dic)
        
        
        while high < N:
            while count != 0 and high < N:
                if s[high] in dic:
                    dic[s[high]] -= 1
                    if dic[s[high]] == 0:
                        count -= 1
                high += 1
                
            if count == 0:
                prev = best
                best = min(best, high - low + 1 )
                if prev > best:
                    res_high, res_low = high, low
            # print(s[res_low:res_high], " : 1st")
            
            while count < 1 and low < high and low < N:
                if s[low] in dic:
                    dic[s[low]] += 1
                    if dic[s[low]] > 0:
                        count += 1
                low += 1
                if count == 0:
                    prev = best
                    best = min(best, high - low + 1 )
                    if prev > best:
                        res_high, res_low = high, low
                
                    
               
            # print(s[res_low:res_high], " : minimized")
                    
        if res_high == 0 and res_low == 0:
            return ""
        else:
            return s[res_low:res_high]
                        
            
        