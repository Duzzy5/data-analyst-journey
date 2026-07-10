```python
import numpy as np

# ==========================================
# Task 1 - Array Arithmetic
# ==========================================

arr = np.array([5, 10, 15, 20, 25])

print("Addition:", arr + 10)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 3)
print("Division:", arr / 5)
print("Power:", arr ** 2)
print("Modulus:", arr % 4)

# ==========================================
# Task 2 - Array vs Array
# ==========================================

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Addition:", a + b)
print("Subtraction:", b - a)
print("Element-wise Multiplication:", a * b)
print("Division:", b / a)

# ==========================================
# Task 3 - Universal Functions
# ==========================================

arr = np.array([16, 25, 36, 49, 64])

print("Square Root:", np.sqrt(arr))
print("Square:", np.square(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

# ==========================================
# Task 4 - Absolute Value
# ==========================================

arr = np.array([-20, -10, 0, 10, 20])

print("Absolute Value:", np.abs(arr))

# ==========================================
# Task 5 - Student Marks
# ==========================================

marks = np.array([45, 67, 89, 90, 34, 76, 58, 99])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

# ==========================================
# Mini Challenge - Salary Bonus
# ==========================================

salary = np.array([25000, 45000, 55000, 60000, 72000])

updated_salary = salary + 5000

print("Updated Salary:", updated_salary)
print("Highest Salary:", np.max(updated_salary))
print("Lowest Salary:", np.min(updated_salary))
print("Average Salary:", np.mean(updated_salary))
```
