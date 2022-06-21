# 1876. Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        N = len(s)
        K = 3
        low = high = 0
        temp = 0
        count = 0
        while high < N:
            while temp < K and high < N:
                temp += 1
                if K==temp:
                    #checking good string
                    # could have made a set so it would be easy to check
                    if s[low] == s[low+1] or s[low] == s[high] or s[low+1] == s[high]:
                        pass
                    else:
                        print(s[low:high+1])

                        count += 1
                high += 1

                
                        
            while low < high and low < N and temp >= K:
                low += 1
                temp -= 1
        return count
            
                
        