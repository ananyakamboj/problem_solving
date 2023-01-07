def my_function(x):
    ans =0
    if (x<0):
        sign = -1
        x= -1 * x
        print("new x")
    else:
        sign = 1
    
    while(x!=0): 
        d = x%10
        ans = ans*10 +d
        x= x//10
    mi = 2 ** (-31)
    ma = 2 ** (31) - 1
    if (ans< mi or ans>ma):
        return 0
    else: 
        return ans * sign

y = my_function(-534)
print(y)


def func2(num):
    initial_number = num
    #reversal 1
    r1 = 0
    while(num!= 0):
        digit = num % 10
        r1 = r1*10 + digit
        num = num//10
    reversed_number = 0
    while (r1!=0):
        digit = r1%10
        reversed_number = reversed_number*10 + digit
        r1 = r1//10
    print("reversed number", reversed_number)
    if reversed_number == initial_number:
        return "true"
    else:
        return "false"

y = func2(1800)
print(y)

#compelement of base10 integer
#decimal to binary
