```python
import numpy as np

# ==========================================
# Task 1 - Scalar Broadcasting
# ==========================================

arr = np.array([10,20,30,40])

print(arr + 10)
print(arr - 5)
print(arr * 2)
print(arr / 10)

# ==========================================
# Task 2 - Subject-wise Bonus
# ==========================================

marks = np.array([
    [80,90,70],
    [60,75,85],
    [95,88,91]
])

bonus = np.array([5,2,3])

print(marks + bonus)

# ==========================================
# Task 3 - Price Increase
# ==========================================

price = np.array([100,250,400,150])

updated_price = price * 1.10

print(updated_price)

# ==========================================
# Task 4 - Broadcasting Prediction
# ==========================================

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20,30])

print(a + b)

# ==========================================
# Task 5 - Incompatible Shapes
# ==========================================

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20])

# Uncomment to observe the error:
# print(a + b)

# ==========================================
# Mini Challenge
# ==========================================

sales = np.array([
    [100,120,140],
    [200,210,220],
    [150,160,170]
])

updated_sales = sales * 1.05

print(updated_sales)
print(np.sum(updated_sales))
print(np.mean(updated_sales))

# ==========================================
# Bonus - 2D Broadcasting
# ==========================================

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10,20,30])

print(a + b)
```
