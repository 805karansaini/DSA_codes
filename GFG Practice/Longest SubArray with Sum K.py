# Longest Sub-Array with Sum K 
# https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1


class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        mydict={0:-1}
        ans=0
        s=0
        for i in range(N):
            s+=A[i]
            
            if s not in mydict:
                mydict[s]=i
            if s-K in mydict:
                ans=max(ans,i-mydict[s-K])
            # print(mydict, ans, s, s-K)
        return ans
    # this solution below doesnot work
    # def lenOfLongSubarr (self, nums, N, K) : 
        
    #     low = high = 0
    #     curr = 0
    #     best = 0
    #     while high < N:
            
    #         while curr <= K and high < N:
    #             curr += nums[high]
    #             # print(low, high, curr, " 1 : curr ")
    #             if curr == K:
    #                 best = max(best, high - low + 1)
    #                 # print(best, low, high)
    #                 high += 1
    #                 break
    #             high += 1
            
            
            
    #         while curr >= K and low <= high and low < N:
    #             curr -= nums[low]
    #             low += 1
    #             if curr == K:
    #                 # print(low, high, curr, " curr ")
    #                 best = max(best, high - low + 1)
    #                 # print(best, low, high)
    #     return best
        
        
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends