# Longest K unique characters substring 
# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1#
# Input:
# S = "aabacbebebe", K = 3
# Output: 7
# Explanation: "cbebebe" is the longest 
# substring with K distinct characters.
#User function Template for python3
from collections import defaultdict
class Solution:

    def longestKSubstr(self, s, k):
        low = high = 0
        N = len(s)
        dic = defaultdict(int)
        best = -1
        while high < N:
            while high < N and len(dic) < k :
                dic[s[high]]+=1
                high += 1
                
            while high < N and s[high] in dic:
                dic[s[high]]+=1
                high += 1
                
            if len(dic)==k:
                best = max(best,high-low)
                
            while len(dic) > k-1:
                if dic[s[low]] == 1:
                    del dic[s[low]]
                else:
                    dic[s[low]] -= 1
                low += 1
        return best
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends