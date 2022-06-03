def sublistRET(p,up):
    liss =  []
    if len(up)==0:
        liss.append(p)
        return liss

    first = sublistRET(p,up[1:])
    lis = [ up[0]  ]
    p = p + lis
    second = sublistRET(p,up[1:])
    first.extend(second)
    return first




up = [1,2,3]
p = []

print(sublistRET(p, up))