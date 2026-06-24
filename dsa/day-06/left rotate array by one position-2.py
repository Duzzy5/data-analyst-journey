#left rotate array by one
arr = [1,2,3,4,5]
def rot(arr):
    drr = arr.copy()
    n = drr[0]
    drr.pop(0)
    drr.append(n)
    return drr
rot(arr)
#the solution is correct but still not a proper dsa way
