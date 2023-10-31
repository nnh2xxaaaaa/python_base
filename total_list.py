def pairSumSequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i,i+1)
        # if i % 2 != 0:
        #     sum += i+2
    return sum

def pairSum(a,b):
    return a + b

def full(n:int):
    if n < 0 :
        return 0

    return n + full( n - 1 )

print(f'sum {pairSumSequence(10)}')
print(f'sum-1 {full(20)}')