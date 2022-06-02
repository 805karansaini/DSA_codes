def subsetRET(p,up):
    lis = []
    if len(up)==0:
        lis.append(p)
        return lis

    c = up[0]
    skip = subset(p,up[1:])
    comb = subset(p+c,up[1:])

    skip.extend(comb)
    return skip



up = "123"
print(subset("",up))