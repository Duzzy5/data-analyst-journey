#largest element in an array

arr = [2, 5, 1, 3, 0]

def lele(arr):
    largest= arr[0]
    for i in range(1,len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    return largest
lele(arr)
