# to remove the duplicates from an array
arr=[1,1,2,2,2,3,3,4]

def dremover(arr):
    drr = arr.copy()
    i = 0
    while i < len(drr)-1:
        if drr[i] == drr[i+1]:
            drr.pop(i)
        else:
            i += 1
    return drr
dremover(arr)
