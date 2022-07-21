def staircase(n):
    if hascache[n-1]:
        return cache[n-1]
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    x = staircase(n-1)
    y = staircase(n-2)
    z = staircase(n-3)
    hascache[n-1] = True
    cache[n-1] = x+y+z

    return x+y+z
n = 100
hascache = [ False ] * n
cache = [ 0 ] * n
print(staircase(n))