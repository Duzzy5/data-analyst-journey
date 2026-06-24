arr = [1,0,2,3,0,4,0,1]
def zerotoend(arr):
    i=0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i=i+1
        else:
            pass
    return arr
zerotoend(arr)
