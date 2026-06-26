def longestSubarray(arr, k):
    prefix_sum = 0
    longest = 0

    # Stores: prefix_sum -> first index where it appeared
    prefix_map = {0: -1}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If (current prefix - k) exists,
        # then the subarray between those indices has sum k.
        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            longest = max(longest, length)

        # Store only the first occurrence
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return longest


arr = [1, -1, 5, -2, 3]
k = 3

print(longestSubarray(arr, k))
