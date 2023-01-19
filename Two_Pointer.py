#sort 0s 1s in O(N)
arr = [1,0,0,1,0,1,0,1,0,0,0,0,1,1,]

def sort0and1(arr):
    i = 0
    j = len(arr)-1
    while(i<j):
        #if there is already 0
        if arr[i]==0:
            i += 1
        elif arr[j] == 1:
            j -= 1
        elif arr[i]==1 and arr[j]==0:
            temp = arr[i]
            arr[i]= arr[j]
            arr[j] = temp
            i += 1
            j -=1
    return arr

sorted_array = sort0and1(arr)
print(sorted_array)

print(sort0and1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]))