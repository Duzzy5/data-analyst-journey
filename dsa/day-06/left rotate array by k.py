#left rotate array by k
arr = [1,2,3,4,5]
d = 2
def rotd(arr):
    i = 0
    for k in range(d):
        arr.append(arr[k])
    for j in range(d,len(arr)):
        arr[i] = arr [j]
        i = i+1
    return arr[:len(arr)-d]
rotd(arr)
