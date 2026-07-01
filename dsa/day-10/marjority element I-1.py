def majorityElement(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    majority = None
    maxFreq = 0

    for key, value in freq.items():
        if value > maxFreq:
            maxFreq = value
            majority = key

    return majority


arr = [2,2,1,1,1,2,2]

print(majorityElement(arr))
