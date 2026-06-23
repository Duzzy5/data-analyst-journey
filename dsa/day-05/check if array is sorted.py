#To check array is sorted or not
arr = [1,2,3,4,5]
def asorted(arr):
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            pass
        else:
            return "not sorted"
    return "sorted"
asorted(arr)
