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

array = [6,7,8,9]
pivot = findPivotMinimum(array)
print(pivot)

even_array =[2,4,6,8,8,8,8,8,12,18]

odd_array = [3,8,11,14,16]

def elementSearch(arr,key):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1

binSearch = elementSearch(even_array, 12)
print("index of 12", binSearch)
binSearch = elementSearch(even_array, 8)
print("index of 8", binSearch)
binSearch = elementSearch(even_array, 0)
print("index of 0", binSearch)

binSearch = elementSearch(odd_array, 11)
print("index of 11", binSearch)
binSearch = elementSearch(odd_array, 16)
print("index of 16", binSearch)
binSearch = elementSearch(odd_array, 1)
print("index of 1", binSearch)

print("good job! :)")

#total number of occurences in a sorted array
def totalOccurence(nums,key):
    def firO(nums,key):
        ans = -1
        start = 0
        end = len(nums) - 1
        while(start <=end):
            mid = start +(end-start)//2
            if nums[mid] == key:
                ans = mid
                end = mid - 1
            elif nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    def lasO(nums,key):
        ans = -1
        start = 0
        end = len(nums) - 1
        while(start <=end):
            mid = start +(end-start)//2
            if nums[mid] == key:
                ans = mid
                start = mid + 1
            elif nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    first_o = firO(nums, key)
    print("first occ", first_o)
    last_o = lasO(nums,key)
    print("last occ", last_o)
    if first_o != -1 or last_o!= -1:
        return (last_o - first_o + 1)
    else:
        return 0

nums = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
key = 8
value = totalOccurence(nums, key)
print("the total no. of occurences of ",key, " is ", value) 

arr = [3, 5, 5, 5, 5, 7, 8, 8]
target = 6
value = totalOccurence(arr, target)
print("the total no. of occurences of ",target, " is ", value)

#peak in mountain array
def peakIndex(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        mid = start + (end - start)//2
        if arr[mid] <= arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start

arr = [0,1,3,10,25,2]
peak = peakIndex(arr)
print("the peak index is ", peak, "and peak/max value is ", arr[peak])
