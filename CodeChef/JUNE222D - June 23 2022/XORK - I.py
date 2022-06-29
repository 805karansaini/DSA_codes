# https://www.codechef.com/JUNE222D/problems/XORK

def solve():
    t = int(input())
    while t:
        t-=1
        n, k = map(int,input().split())
        nums = [*map(int,input().split())]
        # bits , bit, bitmasking, masking, binary
        # bin_list = []
        # for test_num in nums:
        #     bin_list.append([int(i) for i in list('{:032b}'.format(test_num))])
        
        # k = [int(i) for i in list('{:032b}'.format(k))]
            
        
        
        
        val = 0
        j = 0
        best = 10**20
        for i,num in enumerate(nums):
            val = val ^ num
            if val >= k:
                while val >= k:
                    best = min(best, i-j+1)
                    val = val ^ nums[j]
                    j+=1

            while j < i and j < n and val < 1:
                val = val ^ nums[j]
                if val >= k:
                    best = min(best, i-j+1)
                j+=1
        if best == 10**20:
            print("-1")
        else:
            print(best)
                        
solve()