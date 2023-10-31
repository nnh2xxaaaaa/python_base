def sum_int(n:int):
    if n < 0 :
        return 0
    return n + sum_int(n-1)

print(sum_int(3))