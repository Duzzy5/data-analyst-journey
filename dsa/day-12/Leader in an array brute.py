arr = [16,17,4,3,5,2]

def leaders(arr):

    ans = []

    for i in range(len(arr)):

        isLeader = True

        for j in range(i+1, len(arr)):

            if arr[j] > arr[i]:
                isLeader = False
                break

        if isLeader:
            ans.append(arr[i])

    return ans


print(leaders(arr))
