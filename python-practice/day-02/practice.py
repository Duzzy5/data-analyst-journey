```python
import numpy as np

# =====================================
# Task 1 - 1D Indexing
# =====================================

arr = np.array([5, 10, 15, 20, 25, 30])

print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[-2])

# =====================================
# Task 2 - 1D Slicing
# =====================================

print(arr[0:3])

print(arr[-1:-4:-1])

print(arr[1::2])

print(arr[::-1])

# =====================================
# Task 3 - 2D Indexing
# =====================================

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr[0,1])

print(arr[1,2])

print(arr[2,0])

print(arr[2,2])

# =====================================
# Task 4 - 2D Slicing
# =====================================

print(arr[0,:])

print(arr[2,:])

print(arr[:,0])

print(arr[:,2])

# Center Element
print(arr[1,1])

# Top Left 2x2 Matrix
print(arr[0:2,0:2])

# Every Second Row
print(arr[::2])

# Every Second Column
print(arr[:,::2])

# =====================================
# Task 5 - Reshape
# =====================================

arr = np.arange(24)

print(arr.reshape(6,4))

print(arr.reshape(4,6))

print(arr.reshape(2,12))

print(arr.reshape(3,8))

# =====================================
# Bonus Practice
# =====================================

arr = np.arange(1,17).reshape(4,4)

print(arr)

print(arr[1])

print(arr[1,:])

print(arr[:,2])

print(arr[1:4:2,::2])

# =====================================
# Prediction Habit
# =====================================

# Prediction:
# Output -> [5 6 7 8]

print(arr[1])
```
