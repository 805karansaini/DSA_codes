import copy


def removeAll_a_1(s): #return type
    if len(s)==0:
        return ""
    c = s[0]
    p = ""
    if c == "a":
        p = p + removeAll_a_1(s[1:])
    else:
        p = p + c + removeAll_a_1(s[1:])
    return p

s = "abcdaes"
print(removeAll_a_1(s))
#print(removeAll_a(p, up))

def remove_a2(p,up): #print, Do not Return
    if len(up)==0:
        print(p)
        return
    c = up[0]
    if c == "a":
        remove_a2(p,up[1:])
    else:
        remove_a2(p + c, up[1:])

remove_a2("", "abcadea")

# def remove_a(p,up): #print, Do not Return  WAS TESTING RECURSION
#     if len(up)==0:
#         return p
#     c = up[0]
#     if c == "a":
#         p = remove_a(p,up[1:])
#     else:
#         p =  remove_a(p + c, up[1:])
#     return p
# print("hello : ",remove_a("", "abcadea"))