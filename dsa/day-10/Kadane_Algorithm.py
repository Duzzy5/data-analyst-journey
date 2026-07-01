# Maximum Subarray Sum (Kadane's Algorithm)

arr = [-2,1,-3,4,-1,2,1,-5,4]

current = 0
largest = arr[0]

for num in arr:

    current += num

    if current > largest:
        largest = current

    if current < 0:
        current = 0

print(largest)
