#binary search first program

even_array =[2,4,6,8,12,18]

odd_array = [3,8,11,14,16]

def binarySearch(arr, key):
    start_index = 0
    end_index = len(arr)-1
    while(start_index <= end_index):
        print("start ", start_index, "end: ", end_index)
        middle_index = (start_index + end_index)//2


        #optimizng this code

        middle_index = int(start_index + (end_index-start_index)//2)
        print("middle index",middle_index)
        middle_element = arr[middle_index]
        print("middle element", middle_element)
       
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