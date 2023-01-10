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