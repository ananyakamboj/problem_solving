def sqrtInt(n):
    start = 0
    end = n
    ans = 0
    while(start <= end):
        mid = start + (end - start)//2
        if (mid*mid) == n:
            return mid
        elif mid*mid > n:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans

print(sqrtInt(6))

def sqrtDec(n, precision):
    factor = 1
    ans = sqrtInt(n)

    for i in range(precision):
        factor = factor/10
        j = ans
        while j*j < n:
            print("a",j)
            ans = j
            print(factor)
            j = j + factor
            print("b",j)
    return ans

print(sqrtDec(6,2))

