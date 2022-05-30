

def minOpr(a,b,ans):
    if b == c:
        return
    print(b)
    ischange = check(a,b)
    if ischange:
        temp = a[ischange]
        a[ischange] = b.pop(0)
        b.append(temp)
    else:
        for i in range(len(a)):
            if a[i]==0:
                temp = a[i]
                a[i] = b.pop(0)
                b.append(temp)
                print("hellllllwwww")

    minOpr(a,b,ans)
    ans = ans+1
    return ans


def check(a,b):
    print("check")

    n = len(b) - 1
    temp = b[n] + 1
    for i in range(len(a)):
        if a[i]==temp:
            return i
    else:
        return -1


a = [0,0,4,3]
b = [1,0,2,0]
ans = 0
c = [1,2,3,4]
print(minOpr(a,b,ans))
