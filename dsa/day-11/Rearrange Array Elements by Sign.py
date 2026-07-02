arr = [1,-1,-2,2,3,-3]

def alt(arr):
    j=1
    for i in range(1,len(arr)):
        if j < len(arr):
            arr[j], arr[i] = arr[i], arr[j]
            j += 2
        else:
            pass
    return arr
alt(arr)
