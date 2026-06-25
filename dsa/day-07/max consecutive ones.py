# Count Maximum Consecutive Ones

arr = [1,1,0,1,1,1]

def count(arr):

    drr = arr.copy()      
    drr.append(0)         

    a = 0
    arr1 = []

    for i in range(len(drr)):

        if drr[i] == 0:
            arr1.append(a)
            a = 0
        else:
            a += 1

    largest = arr1[0]

    for i in range(1, len(arr1)):

        if arr1[i] > largest:
            largest = arr1[i]

    return largest

print(count(arr))
