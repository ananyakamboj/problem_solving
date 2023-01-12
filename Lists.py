list = [1,2,3,4,5,4,5,6,2,2,1]

list1 = list[2:4]
print(list1)

list2 = list[-3:-1]
print(list2)

list3 = list[::-1]
print(list3)

#list methods
print("LIST METHODS")
#count
print(list.count(2))

#append
list.append(9)
print(list)

#extend
list4= ['a', 'b']
list.extend(list4)
print(list)

#insert
list.insert(0,'hello')
print(list)

#remove
list.remove('b')
print(list)

#pop
list.pop()
print(list)

#copy
#clear
list2 = list.copy()

list.clear()
print("list cleared",list)
print(list2)


#index
print(list2.index(5))

#sort
list2=[1,2,3,3,5,0,-1,3,25]
list2.sort()
print(list2)

#reversing an array
list2.reverse()
print(list2)

#array/list in a function

#passing list as an argument
def printer(a):
    for i in range(len(a)):
        print(a[i])

printer(list2)

#maximum element in a list
print("max element", max(list2))

#minimum element in a list
print("min element",min(list2))


#given an array
#output:sum of elements of the array

print(sum(list2))


#LINEAR SEARCH

def linearSearch(x,y):
    if x in y:
        return True
    else:
        return False

print(linearSearch(4,list2))
print(linearSearch(3,list2))

#using interchanging the elements
def reverseArray(x):
    for i in range(len(x)//2):
        temp = x[i]
        x[i]= x[len(x)-i-1]
        x[len(x)-i-1] = temp
    return x

def reverseArray2(x):
    return x[::-1]


list = [1,2,3,4,5,6,573702,24727,28429,5]
print("Using reverseArray")
print(reverseArray(list))

list = [1,2,3,4,5,6,573702,24727,28429,5]
print("Using reverseArray2")
print(reverseArray2(list))
print(list)


#arrays practice
