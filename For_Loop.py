#sum from 1 to n
n = 3
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum is", sum)

#FIBONACCI Series

a = 0
b = 1
print(a, end = ", ")
for i in range(n-1):
    print(b, end = ", ")
    temp = b
    b = a + b
    a = temp

print ("\n Fibonacci Sequence printed")

#fibonacci using 2 values

a = 0
b = 1
print(a, end = ", ")
for i in range(n-1):
    print(b, end = ", ")
    b = a + b
    a = b - a

print("\n")

#check if a number is prime
#n = 171
for i in range(2,n):
    if(n%i == 0):
        print("Not Prime")
        break
else:
    print("Prime")

#Efficient way
print("Efficient Way: ")
for i in range(2, n//2):
    if (n%i == 0):
        print("Not prime")
        break
else:
    print("Prime")

#CONTINUE Statement

for i in range(5):
    if (i == 2):
        continue
    print(i)

print(2*3/4+5)

#Leetcode question 1
def subtractProductAndSum(n) :
    n = str(n)
    sum = 0
    prod = 1
    for i in n:
        sum += int(i)
        prod *= int(i)
    return (prod - sum)
    
#Leetcode question 2
n = 11111111111111111111111111111101
def hammingWeight(n):
    count = 0
    while(n>0):
        if((n & 1) == 1):
            count +=1
        n = n>>1    
    return count