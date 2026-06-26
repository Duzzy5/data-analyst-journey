arr = [2, 0, 2, 1, 1, 0]

def sort(arr):
    j = 0
    i = 0

    while i < len(arr):

        if arr[i] == 2:
            arr.pop(i)
            arr.append(2)
            # Don't increase i.
            # A new element has come to this index.

        elif arr[i] == 0:
            arr.pop(i)
            arr.insert(j, 0)
            j += 1
            i += 1

        else:
            i += 1

    return arr

print(sort(arr))
