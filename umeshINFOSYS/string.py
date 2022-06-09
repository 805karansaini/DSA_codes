from collections import defaultdict
s = input()

dic = defaultdict(int)
for i in range(len(s)):
    if s[i] == " ":
        continue
    else:
        dic[s[i]] += 1
print(dic)
for i,j in dic.items():
    print(i, " : ", j)