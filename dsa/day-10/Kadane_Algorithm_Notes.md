# Kadane's Algorithm

## Problem

Find the maximum possible sum of a **contiguous subarray**.

Example

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]

Output

6
```

Subarray

```python
[4,-1,2,1]
```

---

# Brute Force Thinking

My approach:

Fix one starting index.

Keep extending the ending index.

Generate every possible contiguous subarray.

Store the maximum sum.

Example

Start = 0

```
[-2]

[-2,1]

[-2,1,-3]

[-2,1,-3,4]
```

Start = 1

```
[1]

[1,-3]

[1,-3,4]
```

Continue until every starting index has been explored.

Time Complexity

```
O(n²)
```

Space Complexity

```
O(1)
```

---

# Observation

Many subarrays begin with a **negative running sum**.

Question:

Can a negative running sum ever help a future subarray?

Example

Current Sum

```
-7
```

Next element

```
10
```

Option 1

```
-7 + 10 = 3
```

Option 2

```
10
```

Starting fresh is always better.

This observation leads to Kadane's Algorithm.

---

# Kadane's Intuition

If the running sum becomes negative,

discard it.

A negative prefix can only reduce the sum of future subarrays.

Instead of checking every possible starting index,

Kadane automatically decides whether to

- continue the current subarray, or
- start a new one.

---

# Algorithm

Initialize

```python
current = 0
largest = arr[0]
```

Traverse the array.

For every number

```python
current += num
```

Update

```python
largest = max(largest, current)
```

If

```python
current < 0
```

Reset

```python
current = 0
```

Continue.

---

# Code

```python
current = 0
largest = arr[0]

for num in arr:

    current += num

    if current > largest:
        largest = current

    if current < 0:
        current = 0

print(largest)
```

---

# Dry Run

```
Array

[-2,1,-3,4,-1,2,1,-5,4]
```

| Number | Current Sum | Largest |
|---------|------------:|---------:|
| -2 | -2 | -2 |
| Reset | 0 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| Reset | 0 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

Answer = **6**

---

# Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

# Limitations

This version correctly handles

- Positive arrays
- Negative arrays
- Mixed arrays

Only because

```python
largest = arr[0]
```

If

```python
largest = 0
```

then

```python
[-5,-2,-7]
```

incorrectly returns

```
0
```

instead of

```
-2
```

---

# Pattern Recognition

Use Kadane when the question contains words like

- Maximum Subarray Sum
- Maximum Contiguous Sum
- Largest Sum of Consecutive Elements
- Best Continuous Segment

---

# Biggest Learning

## Brute Force

Outer loop chooses the starting index.

Inner loop extends the ending index.

Generates every possible contiguous subarray.

---

## Kadane

Never carry a negative running sum.

If the current sum becomes negative,

throw it away and start fresh.

---

# Brick of the Day 🧱

**Brute Force asks:**

> "What is the sum of every possible subarray?"

**Kadane asks:**

> "Is my current subarray still worth keeping?"

If the answer is **No**, start a new subarray.
