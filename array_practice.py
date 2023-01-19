#swapping two alternate elements in an array

arr = [1,2,7,8,5,6]
def swapAlternate(arr):
    for i in range(0,len(arr),2):
        if (i+1)<len(arr):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

    return arr
answer = swapAlternate(arr)
print(answer)


#finding unique element in arr
arr = [2,3,1,6,6,2,3]

def unique_Element(arr):
    answer = 0
    for i in arr:
        answer = answer ^ i
    return answer

answer = unique_Element(arr)
print(answer)

a = [1,2,3]
b= [1,2,4]
print(set(a)-set(b))
print(set(a)^set(b))

d = {1:2, 2:3 }
for i in d:
    print(i, d[i])


print(list(range(5)))

#duplicates in an array
def duplicate(arr):
    l = list(range(1,len(arr)))
    print("initial l", l)
    l.extend(arr)
    print("l now", l)
    answer = 0
    for i in l:
        answer = answer ^ i
        #print(answer)
    return answer

arr = [5,4,1,2,6,3,5]
answer = duplicate(arr)
print(answer)

a = [1,2,3]
b = [2,3,4]
c= [0,0,0]
d = [0,0,0]

print(set(a)&set(b))
target = 10
a = list(range(6))
for i in range(len(a)):
    f = a[i]
    for j in a[i+1:]:
        s = a[j]
        t = target-f-s
        if t in a[j+1:]:
            value = [f,s,t]
            print(value)

