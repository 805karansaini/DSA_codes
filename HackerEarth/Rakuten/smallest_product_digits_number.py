# give a number k ( 1 <= k < 5 * 10** 5)
# return the number ( k - digits) that have sumofdigits <= product of digits.
# product should be minimum, if multiple solution exist return the smallest number
from collections import defaultdict
def smallest_number(K):
    ans = [1]*K
    dic = defaultdict(list)
    mini = 500000000
    left = K-7
    seen = set()
    for i1 in range(1,10):
        for i2 in range(1,10):
            for i3 in range(1,10):
                for i4 in range(1,10):
                    for i5 in range(1,10):
                        for i6 in range(1,10):
                            for i7 in range(1,10):
                                tempset = [i1,i2,i3,i4,i5,i6,i7]
                                tempset.sort()
                                num = int("".join(map(str,tempset)))               
                                if num in seen:
                                    break
                                seen.add(num)
                                mul = i1*i2*i3*i4*i5*i6*i7
                                if (left+i1+i2+i3+i4+i5+i6+i7) <= mul:
                                    if mini >= mul:
                                        mini = mul
                                        dic[mul].append(num)
                                     
    dic = dict(sorted(dic.items(), key=lambda item: item[0]))
    for i,j in dic.items():
        j.sort()
        answer = j[0]
        ansback = str(answer)
        break
    if K < 8:
        return ansback[-K:]  
    else:
        return ("".join(map(str,ans[:K-7])) + ansback)


T = int(input())
for _ in range(T):
    K = int(input())

    out_ = smallest_number(K)
    print (out_)