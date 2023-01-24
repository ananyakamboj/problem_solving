#binary search first program

even_array =[2,4,6,8,8,8,8,8,12,18,]

odd_array = [3,8,11,14,16]

def binarySearch(arr, key):
    start_index = 0
    end_index = len(arr)-1
    while(start_index <= end_index):
       # print("start ", start_index, "end: ", end_index)
        middle_index = (start_index + end_index)//2
        #optimizng this code
        middle_index = int(start_index + (end_index-start_index)//2)
       # print("middle index",middle_index)
        middle_element = arr[middle_index]
        #print("middle element", middle_element)
       
        if middle_element == key:
            return middle_index
        #go to right part
        elif middle_element < key:
            start_index = middle_index + 1
            #arr = arr[start_index:]
            #print("right part", arr)
        #go to left part
        else:
            end_index = middle_index-1
            #arr = arr[:middle_index]
            #print("left part", arr)
    return  -1

my_index = binarySearch(even_array,19)
print("my_index", my_index)

my_index = binarySearch(odd_array,11)
print("my_index", my_index)

#binary search finding first and last element
def firstLastElement(arr,key):
    start_i = 0
    end_i = len(arr)-1
    first_o = -1
    last_o = -1 
    while(start_i<=end_i):
        mid_i = start_i + (end_i-start_i)//2
        if arr[mid_i] == key:
            first_o = mid_i
            end_i = mid_i-1
        elif arr[mid_i]<key:
            start_i = mid_i + 1
        else:
            end_i = mid_i - 1
    start_i = 0
    end_i = len(arr)-1
    while(start_i<=end_i):
        mid_i = start_i + (end_i-start_i)//2

        if arr[mid_i] == key:
            last_o = mid_i
            start_i = mid_i + 1
        elif arr[mid_i]<key:
            start_i = mid_i + 1
        else:
            end_i = mid_i - 1
    return [first_o, last_o]

a = firstLastElement(even_array, 8)
print(a)


#find pivot in array: minimum element
def findPivotMinimum(arr):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    while(start < end):
        mid = (start+end)//2
        if arr[0]<= arr[mid]:
            start = mid + 1
        else:
            end = mid
    return start

array = [6,7,8,9,2,3]
pivot = findPivotMinimum(array)
print(pivot)