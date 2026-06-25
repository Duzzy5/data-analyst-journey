arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

def merge(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    arr3 = []

    i = 0
    j = 0

    while i < n and j < m:

        if arr1[i] > arr2[j]:

            if len(arr3) == 0 or arr3[-1] != arr2[j]:
                arr3.append(arr2[j])

            j += 1

        elif arr1[i] < arr2[j]:

            if len(arr3) == 0 or arr3[-1] != arr1[i]:
                arr3.append(arr1[i])

            i += 1

        else:

            if len(arr3) == 0 or arr3[-1] != arr1[i]:
                arr3.append(arr1[i])

            i += 1
            j += 1

    # Remaining elements of arr1
    while i < n:

        if len(arr3) == 0 or arr3[-1] != arr1[i]:
            arr3.append(arr1[i])

        i += 1

    # Remaining elements of arr2
    while j < m:

        if len(arr3) == 0 or arr3[-1] != arr2[j]:
            arr3.append(arr2[j])

        j += 1

    return arr3


print(merge(arr1, arr2))
