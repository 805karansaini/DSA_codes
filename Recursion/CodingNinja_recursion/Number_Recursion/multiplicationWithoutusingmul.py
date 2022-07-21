def multi(num, mul):
    if mul == 1:
        return num
    return num + multi(num, mul-1)

print(multi(4,10))