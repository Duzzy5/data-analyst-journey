def twoSum(arr, target):
    mp = {}

    for i in range(len(arr)):

        need = target - arr[i]

        if need in mp:
            return [mp[need], i]

        mp[arr[i]] = i

    return [-1, -1]


arr = [3, 2, 4]
target = 6

print(twoSum(arr, target))
