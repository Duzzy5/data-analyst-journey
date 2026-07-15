```python
import numpy as np

# ==========================================
# Task 1 - Transpose
# ==========================================

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("Original Shape:", arr.shape)
print("Transpose:")
print(arr.T)
print("Transpose Shape:", arr.T.shape)

# ==========================================
# Task 2 - Dot Product
# ==========================================

a = np.array([2,3,4])
b = np.array([5,6,7])

print("Element-wise Multiplication:", a * b)
print("Dot Product:", np.dot(a,b))

# ==========================================
# Task 3 - Matrix Multiplication
# ==========================================

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print("Element-wise:")
print(a * b)

print("Matrix Multiplication:")
print(a @ b)

# ==========================================
# Task 4 - Identity Matrix
# ==========================================

print(np.eye(4))

# ==========================================
# Task 5 - Matrix Inverse
# ==========================================

A = np.array([
    [4,7],
    [2,6]
])

print(np.linalg.inv(A))

# ==========================================
# Mini Challenge
# ==========================================

exam1 = np.array([80,90,70])
exam2 = np.array([75,95,85])

print("Subject-wise Total:", exam1 + exam2)
print("Dot Product:", np.dot(exam1, exam2))
```
