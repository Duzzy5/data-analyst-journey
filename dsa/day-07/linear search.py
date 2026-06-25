arr = [10, 25, 7, 18, 30]
target = 18

def linear_search(arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
        else:
            pass
    return -1

linear_search(arr)
