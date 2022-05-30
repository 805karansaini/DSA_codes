#
#
# i = 1234
#
# print(i%10)
# print(int((i%100)/10))
# print(i//1000)
# print((i//100)%10)
d1 = 9
d2 = 9


def count_ret(d1,d2):
    count = 0
    for i in range(0,10000):
        if i > 999:
            if d1 == abs( int(i//1000) - int(((i//100)%10)) ) and d2 == abs(i%10 - int((i%100)/10)):
                print(i)
                count+=1
        else:
            number_str = str(i)
            zero_filled_number = number_str.zfill(4)
            i = int(zero_filled_number)
            if d1 == abs( int(i//1000) - int(((i//100)%10)) ) and d2 == abs(i%10 - int((i%100)/10)):
                print(i)
                count+=1
    return count


# t = int(input())
d1d2 = input()
print(d1d2)
inp = d1d2.split())

print(count_ret(d1,d2))


