arr = [1,1,0,1,1,1]

def count(arr):

    current = 0
    largest = 0

    for i in range(len(arr)):

        if arr[i] == 1:
            current += 1

            if current > largest:
                largest = current

        else:
            current = 0

    return largest
