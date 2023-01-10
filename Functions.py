#functions

#power
def power(a,b):
    return a**b
x = power(5,5)
print(x)

#isEven
def isEven(a):
    if a%2==0:
        return True
    else:
        return False
x = isEven(10)
print(x)

#nCr
def factorial(n):
    if n==0:
        return 1
    else:
        factorial = 1
        while(n>0):
            factorial = factorial * n
            n-=1
        return factorial

x = factorial(6)
print(x)

def combination(n,r):
    numerator = factorial(n)
    denominator = factorial(r)*factorial(n-r)
    return numerator/denominator

x = combination(5,4)
print(x)

#print COUNTING
def counting(n):
    for i in range(1,n+1):
        print(i)
    return None

counting(10)

#isPrime
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(isPrime(91))

#AP
def aProgression(n):
    return (3*n)+7

x= aProgression(3)
print(x)

def decToBin(n):
    answer = 0
    count = 0
    while(n!=0):
        digit = n%2
        answer = digit * pow(10,count)+ answer
        n = n>>1
        count += 1
    return answer
x = decToBin(20)
print(x)

#Total No. of set bits
def setBits(a,b):
    #convert into binary
    bin_a = decToBin(a)
    bin_b = decToBin(b)

    count_a = 0
    count_b =0
    
    while(bin_a!=0):
        if bin_a%2 == 1:
            count_a += 1
        bin_a = bin_a // 10
    
    while(bin_b!=0):
        if bin_b%2 == 1:
            count_b += 1
        bin_b = bin_b // 10    
    
    return count_a + count_b

x = setBits(5,3)
print(x)

#fibonacci 
def fib(n):
    a = 0
    b = 1
    while(n!=0):
        #print(a, end=" ")
        b = a + b
        a = b - a 
        #b = next
        n -=1
    return a

print(fib(9))

def dummy(n):
    n= n+1
    return n

n = 15
o = dummy(n)  
print("n", n, "o", o)
