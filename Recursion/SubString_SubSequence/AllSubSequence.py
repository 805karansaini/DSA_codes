def all(p,list):
    if len(list) < 1:
        return


    p = p + [list[0]] + all(p,list[1:])
    p = p + all(p, list[1:])

    return p



list = [1,2,3]
p = []
print(all(p,list))
