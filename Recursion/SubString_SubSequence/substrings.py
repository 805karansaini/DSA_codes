def subRET(p, up):
    if len(up)==0:
        return p + " "
    c = up[0]
    skip = subRET(p,up[1:])
    com = subRET(p + c, up[1:])
    temp = skip + com
    return temp



s = "abc"
print(subRET("",s))

def sub(p,up):
    if len(up)==0:
        print(p)
        return
    c = up[0]
    sub(p,up[1:])
    sub(p+c,up[1:])




s = "123"
print(sub("",s))