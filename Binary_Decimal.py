#Converting a Decimal into Binary
def decimalToBinary(n):
    count = 0
    answer = 0
    while(n!=0):
        x = n%2
        if (x%2 == 1):
            digit = 1
        else:
            digit = 0
        n = n>>1
        answer = (digit * pow(10, count)) + answer
        count += 1
    return answer

print(decimalToBinary(7))
print(decimalToBinary(8))


def negDecimalToBinary(n):
    n = n * (-1)
    print("new ", n)
    count = 0
    answer = 0
    while(n!=0):
        x = n%10
        if (x%2 == 1):
            digit = 0
        else:
            digit = 1
        n = n>>1
        answer = (digit * pow(10, count)) + answer
        count += 1
    return answer

print(negDecimalToBinary(-8))

def binaryAddition(n):
    count = 0
    count2 = 0
    answer = 0
    if (n&1) == 0:
        return n+1
    else:
        while(n!=0):
            if (n&1)==1:
                digit = 1
            else: 
                if count2 <1:
                    digit = 1
                    count2 +=1
                else: 
                    digit = 0
            n = n>>1
            answer = (digit * pow(10, count)) + answer
            count += 1
        return answer

#print("A", binaryAddition(101))

#stuck at Binary Bitwise Addition

#Binary to Decimal

def binaryToDecimal(n):
    #print("n" ,n)
    count = 0
    answer = 0
    while(n!=0):
        #print("Count",count)
        x = n % 10
        #print("X :", x)     
        answer = (x * (pow(2, count))) + answer
        #print("answer", answer)
        n = n//10
        #print ("New N", n)
        count += 1
    return answer

print(binaryToDecimal(101))

print(~101)