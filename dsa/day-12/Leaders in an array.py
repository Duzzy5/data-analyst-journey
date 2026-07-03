arr = [16,17,4,3,5,2]

def leaders(arr):

    leader = []

    largest = arr[-1]

    leader.append(largest)

    for i in range(len(arr)-2, -1, -1):

        if arr[i] > largest:

            largest = arr[i]

            leader.append(arr[i])

    return leader[::-1]


print(leaders(arr))
