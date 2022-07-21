def countzero(n):
    temp = n%10
    rem = n//10
    if temp == n:# as number can start with leading zeros
        return 0
    if temp == 0:
        return 1 + countzero(rem)
    else:
        return 0 + countzero(rem)

n = 1000008900029
print(countzero(n))