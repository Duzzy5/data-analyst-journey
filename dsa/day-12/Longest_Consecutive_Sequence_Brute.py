arr = [0,3,7,2,5,8,4,6,0,1]

arr.sort()

def consecutive(arr):

    if len(arr) == 0:
        return 0

    current = 1
    longest = 1

    for i in range(len(arr)-1):

        if arr[i] == arr[i+1]:
            continue

        elif arr[i] + 1 == arr[i+1]:

            current += 1

            if current > longest:
                longest = current

        else:
            current = 1

    return longest


print(consecutive(arr))
