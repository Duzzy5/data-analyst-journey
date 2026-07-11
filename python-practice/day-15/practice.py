```python
import numpy as np

# ==========================================
# Task 1 - Aggregation Functions
# ==========================================

arr = np.array([15, 25, 35, 45, 55])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# ==========================================
# Task 2 - Aggregation with Axis
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Total Sum:", np.sum(arr))
print("Column-wise Sum:", np.sum(arr, axis=0))
print("Row-wise Sum:", np.sum(arr, axis=1))

print("Column-wise Mean:", np.mean(arr, axis=0))
print("Row-wise Mean:", np.mean(arr, axis=1))

# ==========================================
# Task 3 - Student Marks
# ==========================================

marks = np.array([
    [85, 90, 95],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 70]
])

print("Average of Each Student:", np.mean(marks, axis=1))
print("Average of Each Subject:", np.mean(marks, axis=0))

print("Highest Mark in Each Subject:", np.max(marks, axis=0))
print("Lowest Mark of Each Student:", np.min(marks, axis=1))

# ==========================================
# Task 4 - Temperature Analysis
# ==========================================

temp = np.array([
    [31, 33, 30, 29],
    [35, 36, 34, 33],
    [28, 27, 29, 30]
])

print("Average Temperature of Each City:", np.mean(temp, axis=1))
print("Highest Temperature of Each City:", np.max(temp, axis=1))
print("Average Temperature of Each Day:", np.mean(temp, axis=0))

# ==========================================
# Mini Challenge - Company Profit
# ==========================================

profit = np.array([
    [12, 15, 18, 20],
    [10, 14, 16, 22],
    [18, 19, 17, 25]
])

print("Total Yearly Profit of Each Company:")
print(np.sum(profit, axis=1))

print("Average Profit of Each Quarter:")
print(np.mean(profit, axis=0))

highest_profit = np.max(profit)

print("Highest Single Quarter Profit:", highest_profit)
```
