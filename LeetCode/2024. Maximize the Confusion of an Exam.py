# 2024. Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.
# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        count = Counter(s)
        if count["T"] <= k or count["F"] <= k:
            return len(s)
        N = len(s)
        
        # considering T as 1 and F as 0. to Find max len
        
        high = low = best = res = 0
        temp = k
        while high < N:
            while high < N and temp > 0:
                if s[high] == "F":
                    temp -= 1
                best += 1
                high += 1
            
            while high < N and s[high] == "T":
                best += 1
                high += 1
            res = max(res,best)
            
            while temp < 1 and low <= high and low < N:
                if s[low]=="F":
                    temp += 1
                best -= 1
                low += 1
        res1 = max(res,best)
        
        
        # considering F as 1 and T as 0. to Find max len
        high = low = best = res = 0
        temp = k
        while high < N:
            while high < N and temp > 0:
                if s[high] == "T":
                    temp -= 1
                best += 1
                high += 1
            
            while high < N and s[high] == "F":
                best += 1
                high += 1
            res = max(res,best)
            
            while temp < 1 and low <= high and low < N:
                if s[low]=="T":
                    temp += 1
                best -= 1
                low += 1
            
        res2 = max(res,best)
        
        return max(res2,res1)
                
        