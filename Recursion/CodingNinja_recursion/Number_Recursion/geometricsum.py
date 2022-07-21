def geo(n,start,mul):
    prev = start
    if n == 1:
        return prev
    start *= mul
    return prev + geo(n-1,start,mul)
print(geo(3,1,2)) # 1 + 2 + 2 (3,1,2)
print(geo(3,1,0.5)) 
print(geo(5,1,0.5)) 