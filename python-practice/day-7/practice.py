```python
import numpy as np

# ==========================================
# Task 1 - Sorting
# ==========================================

arr = np.array([50,20,80,40,10])

print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])

# ==========================================
# Task 2 - Sorting 2D Arrays
# ==========================================

arr = np.array([
    [8,2,5],
    [3,9,1]
])

print("Row-wise Sort:")
print(np.sort(arr))

print("Column-wise Sort:")
print(np.sort(arr, axis=0))

# ==========================================
# Task 3 - Unique Values
# ==========================================

arr = np.array([1,2,2,3,4,4,5,5,5])

print(np.unique(arr))
print(np.unique(arr, return_counts=True))

# ==========================================
# Task 4 - Searching
# ==========================================

marks = np.array([45,82,91,36,78,91])

print(np.where(marks == 91))
print(np.where(marks < 50))
print(marks[marks > 80])

# ==========================================
# Mini Challenge
# ==========================================

emp_id = np.array([
    101,
    103,
    102,
    101,
    105,
    104,
    102,
    103
])

print(np.unique(emp_id))
print(np.unique(emp_id, return_counts=True))
print(np.sort(emp_id))
print(np.sort(emp_id)[::-1])
```
