#two sums
arr = [3, 2, 4]
target = 6

def ts(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target :
                return i,j
            else:
                pass
    return "Not Found"

ts(arr,target)
