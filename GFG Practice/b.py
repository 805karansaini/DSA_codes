def getMinimumCost(parcels, k):
    N = len(parcels)
    if N == k:
        return 0
    seen = set(parcels)
    req = k-N
    res = 0
    i = 1
    while req:
        if i in seen:
            i+=1
            continue
        else:
            req-=1
            res += i
            i += 1
    return res

print(getMinimumCost([2,3,6,10,11],9))