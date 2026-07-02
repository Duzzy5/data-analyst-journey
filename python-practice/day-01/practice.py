# NumPy Day 1 Practice

```python
import numpy as np

# -----------------------------
# Task 1
# -----------------------------

arr1 = np.array([1, 2, 3])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr3 = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 0], [0, 9]],
    [[8, 7], [6, 5], [4, 3]]
])

for arr in [arr1, arr2, arr3]:
    print("--------------------")
    print(arr)
    print("Shape :", arr.shape)
    print("Dimensions :", arr.ndim)
    print("Size :", arr.size)
    print("Dtype :", arr.dtype)

# -----------------------------
# Task 2
# -----------------------------

print(np.zeros(10))

print(np.ones(10))

print(np.eye(5))

print(np.arange(10, 50))

print(np.linspace(0, 1, 20))

# -----------------------------
# Task 3
# -----------------------------

arrays = [
    np.array([1,2,3], dtype=np.int32),
    np.array([1,2,3], dtype=np.int64),
    np.array([1,2,3], dtype=np.float32),
    np.array([1,2,3], dtype=np.float64)
]

for arr in arrays:
    print("--------------------")
    print(arr.dtype)
    print("Shape :", arr.shape)
    print("Size :", arr.size)
    print("Itemsize :", arr.itemsize)
    print("Total Bytes :", arr.nbytes)

# -----------------------------
# Task 4
# -----------------------------

arr = np.array([
    [[1,2],[3,4],[5,6]],
    [[7,8],[9,0],[0,9]],
    [[8,7],[6,5],[4,3]]
], dtype=np.int32)

print("Itemsize :", arr.itemsize)
print("Total Bytes :", arr.nbytes)

# -----------------------------
# Mini Challenge
# -----------------------------

print(np.full((3,3), 7))

# -----------------------------
# Stretch Challenge
# -----------------------------

print(np.eye(3))
```
