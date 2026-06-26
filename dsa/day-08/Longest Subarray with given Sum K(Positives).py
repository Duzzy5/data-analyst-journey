def longestSubarray(arr, k):
    left = 0
    right = 0
    current_sum = 0
    longest = 0

    while right < len(arr):

        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            longest = max(longest, right - left + 1)

        right += 1

    return longest
