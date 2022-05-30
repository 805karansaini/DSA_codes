def largestGoodInteger( num):
    N = len(num)
    mylist = []
    res = ""
    for i in range(N - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            res = num[i] + num[i + 1] + num[i + 2]
            mylist.append(res)
            print(mylist,max(mylist))
    res = ""
    type()
    if mylist:
        return str(max(mylist))
    return ""

num = "677713333999"

print(largestGoodInteger(num))