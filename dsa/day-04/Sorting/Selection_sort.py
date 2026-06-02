#selection sort ascending
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[3,5,2,1,4]
selection_sort(arr)

#selection sort descending
ar=[2,3,4,1,5]
def ds_sort(ar):
    x=0
    n=len(ar)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if ar[min_index]<ar[j]:
                min_index = j
        ar[i],ar[min_index]=ar[min_index],ar[i]
    return ar,
ds_sort(ar)
