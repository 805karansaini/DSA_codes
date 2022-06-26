# https://www.codechef.com/JUNE222D/problems/STRNG
from collections import defaultdict
from copy import deepcopy
def solve():

    def gcd(a,b):
        if (b == 0):
            return a
        return gcd(b, a%b)
    def list_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    t = int(input())
    while t:
        print()
        print()
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        if n ==3:
            strong = 0
            if gcd(nums[0],nums[1]) > 1:
                strong += 1
            if gcd(nums[0],nums[2]) > 1:
                strong += 1
            if gcd(nums[2],nums[1]) > 1:
                strong += 1
            print(strong)
            continue
            
        num1 = nums[0]
        num2 = nums[1]
        if n == 2:
            if num1 == 1 and num2 == 1:
                print("0")
            elif num1 > 1 and num2 > 1:
                print("2")
            else:
                print("1")
            continue
        temp_gdc = []
        
        L_gdc = list_gcd(num1,num2)
        temp_gdc.append(L_gdc)
        for i in range(2,n):
            L_gdc = list_gcd(L_gdc,nums[i])
            temp_gdc.append(L_gdc)

        if L_gdc > 1:
            print(n, " printed as L_gdc > 1")
            continue
        
        copynums = nums[::-1]
        num1 = copynums[0]
        num2 = copynums[1]
        rev_gdc = []

        R_gdc = list_gcd(num1,num2)
        rev_gdc.append(R_gdc)
        for i in range(2,n):
            R_gdc = list_gcd(R_gdc,copynums[i])
            rev_gdc.append(R_gdc)
        rev_gdc = rev_gdc[::-1]
        print(temp_gdc)
        print(rev_gdc)
        if n == 4:
            strong = 0
            # skiping last two numbers
            if temp_gdc[n-3] > 1: # last
                strong += 1
            if gcd(temp_gdc[n-4],nums[n-1]) > 1: # second last gcd(temp_gcd[n-3], nums[n-1])
                strong += 1
            # skipping first two numbers
            if rev_gdc[1] > 1: # first 0th index
                strong += 1
            if gcd(rev_gdc[2],nums[0]) > 1: # second 1st index gcd(rev_gdc[2], nums[0])
                strong += 1
            print(strong, " : strong above")
        else:
            strong = 0
            # skiping last two numbers
            if temp_gdc[n-3] > 1: # last
                strong += 1
            if gcd(temp_gdc[n-4],nums[n-1]) > 1: # second last gcd(temp_gcd[n-3], nums[n-1])
                strong += 1
            # skipping first two numbers
            if rev_gdc[1] > 1: # first 0th index
                strong += 1
            if gcd(rev_gdc[2],nums[0]) > 1: # second 1st index gcd(rev_gdc[2], nums[0])
                strong += 1
            for i in range(2,n-2):
                if gcd(temp_gdc[i-2],rev_gdc[i+1]) > 1:
                    strong += 1     
            print(strong, " : strong, below")
solve()


