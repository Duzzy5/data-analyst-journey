```python
import numpy as np

# ==========================================
# Task 1 - Boolean Comparisons
# ==========================================

arr = np.array([12, 25, 38, 41, 56, 63])

print("Greater than 40:", arr > 40)
print("Less than 30:", arr < 30)
print("Equal to 38:", arr == 38)
print("Not Equal to 25:", arr != 25)

# ==========================================
# Task 2 - Boolean Indexing
# ==========================================

print("Elements greater than 40:", arr[arr > 40])
print("Elements less than 30:", arr[arr < 30])
print("Even numbers:", arr[arr % 2 == 0])

# ==========================================
# Task 3 - Student Marks
# ==========================================

marks = np.array([45, 67, 89, 90, 34, 76, 58, 99])

print("Above 75:", marks[marks > 75])
print("Below 50:", marks[marks < 50])
print("Between 60 and 90:", marks[(marks > 60) & (marks < 90)])
print("Exactly 90:", marks[marks == 90])

# ==========================================
# Task 4 - Fancy Indexing (1D)
# ==========================================

arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Selected Elements:", arr[[1, 4, 6]])

# ==========================================
# Task 5 - Fancy Indexing (2D)
# ==========================================

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print("First and Fourth Row:")
print(arr[[0, 3]])

print("Second and Third Row:")
print(arr[[1, 2]])

# ==========================================
# Mini Challenge - Salary Filtering
# ==========================================

salary = np.array([
    25000,
    45000,
    55000,
    60000,
    72000,
    35000,
    90000
])

print("Salary Above 50000:")
print(salary[salary > 50000])

print("Salary Below 40000:")
print(salary[salary < 40000])

print("Salary Between 40000 and 80000:")
print(salary[(salary > 40000) & (salary < 80000)])

# ==========================================
# Bonus Examples
# ==========================================

print("Indices 0, 2, 5:")
print(arr[[0, 2]])

numbers = np.array([5, 10, 15, 20, 25])

print("Numbers divisible by 5:")
print(numbers[numbers % 5 == 0])

print("Numbers greater than 12:")
print(numbers[numbers > 12])
```
