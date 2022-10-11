def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums = [*map(int,input().split())]


        Result = N
        temp_req = 0

        for indx in range(N):
            temp_req += nums[indx]
            final_Res = indx + 1

            left = indx + 1
            temp_count = 0
            prev = left
            flag = True
            while left < N:
                flag = False
                temp_count += nums[left]
                left += 1
                if temp_count == temp_req:
                    temp_count = 0
                    final_Res = max(final_Res, left - prev)
                    prev = left
                    flag = True
                elif temp_count > temp_req:
                    flag = False
                    break
            # print(indx, flag, left, final_Res, Result)
            if left == N and flag:
                Result = min(Result, final_Res)
        
        print(Result)
solve()