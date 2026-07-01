# Maximum Subarray Sum (Brute Force)

arr = [-2,1,-3,4,-1,2,1,-5,4]

largest = arr[0]

for i in range(len(arr)):

    current = 0

    for j in range(i, len(arr)):

        current += arr[j]

        if current > largest:
            largest = current

print(largest)
