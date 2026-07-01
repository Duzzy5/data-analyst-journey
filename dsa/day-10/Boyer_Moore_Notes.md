# Boyer-Moore Voting Algorithm

## Problem

Find the **Majority Element** in an array.

A Majority Element is an element that appears **more than n/2 times**.

Example:

```python
arr = [2,2,1,1,1,2,2]

Output:
2
```

---

# Intuition

Imagine every element is a candidate in an election.

Whenever **two different elements** meet, they cancel each other.

Example:

```
2 vs 1

↓

Both are cancelled.
```

Since the majority element appears **more than all other elements combined**, it can never be completely cancelled.

Eventually, only the majority element survives.

---

# Algorithm

Maintain two variables:

```python
candidate = None
count = 0
```

Traverse the array.

### Rule 1

If

```python
count == 0
```

Choose the current element as the new candidate.

---

### Rule 2

If the current element is the candidate,

```python
count += 1
```

---

### Rule 3

Otherwise,

```python
count -= 1
```

---

At the end,

`candidate` will be the majority element (if one is guaranteed to exist).

---

# Dry Run

```python
arr = [2,2,1,1,1,2,2]
```

| Element | Candidate | Count |
|---------|-----------|------:|
|2|2|1|
|2|2|2|
|1|2|1|
|1|2|0|
|1|1|1|
|2|1|0|
|2|2|1|

Final Candidate = **2**

---

# Code

```python
def majorityElement(arr):

    candidate = None
    count = 0

    for num in arr:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


arr = [2,2,1,1,1,2,2]

print(majorityElement(arr))
```

---

# Complexity

Time Complexity

```
O(n)
```

Space Complexity

```
O(1)
```

---

# Why Does It Work?

Suppose

```
2 2 2 2 1 3 4
```

There are four `2`s and only three non-`2`s.

Every non-`2` can cancel only one `2`.

```
2 × 1

↓

Cancelled
```

After all cancellations, at least one `2` will always remain.

Hence, the final candidate must be the majority element.

---

# Limitation

This algorithm assumes that a majority element **exists**.

If the problem does **not** guarantee a majority element, perform one extra verification pass.

```python
candidate = majorityElement(arr)

count = 0

for num in arr:
    if num == candidate:
        count += 1

if count > len(arr)//2:
    return candidate
else:
    return -1
```

---

# Comparison

| HashMap | Boyer-Moore |
|---------|-------------|
| O(n) Time | O(n) Time |
| O(n) Space | O(1) Space |
| Counts every frequency | Cancels different elements |
| Easier to understand | Requires intuition |

---

# Pattern Recognition

Use Boyer-Moore when:

- The problem asks for the **Majority Element**.
- The majority element is guaranteed to exist.
- Space optimization is required.

Use HashMap when:

- Frequencies are required.
- Majority is **not** guaranteed.
- You need counts of all elements.

---

# Revision in One Minute

✔ Candidate stores the possible majority.

✔ Count represents the current vote balance.

✔ Same element → Increase count.

✔ Different element → Decrease count.

✔ Count becomes 0 → Choose a new candidate.

✔ If majority exists, it always survives all cancellations.

---

# Brick of the Day 🧱

**HashMap asks:**

> "How many times does each element appear?"

**Boyer-Moore asks:**

> "Which element cannot be completely cancelled?"
