#Second largest element in an array
arr = [2, 5, 1, 10]

def lele(drr):
    largest= arr[0]
    slarge = arr[1]
    if slarge>largest:
        largest, slarge = slarge, largest
    for i in range(1,len(drr)):
        if arr[i]>largest:
            slarge = largest
            largest = arr[i]
        elif arr[i] > slarge and arr[i] != largest:
            slarge = arr[i]
        else:
            pass
    return slarge
lele(arr)
