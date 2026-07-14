```python
import numpy as np

# ==========================================
# Task 1 - Random Integers
# ==========================================

print(np.random.randint(1, 50))
print(np.random.randint(10, 100, size=5))

# ==========================================
# Task 2 - Random Floats
# ==========================================

print(np.random.rand())
print(np.random.rand(5))
print(np.random.rand(3,3))

# ==========================================
# Task 3 - Random Choice
# ==========================================

colors = np.array([
    "Red",
    "Blue",
    "Green",
    "Black",
    "White"
])

print(np.random.choice(colors))
print(np.random.choice(colors, size=3))

# ==========================================
# Task 4 - Shuffle
# ==========================================

arr = np.arange(1,11)

print("Before Shuffle:", arr)

np.random.shuffle(arr)

print("After Shuffle:", arr)

# ==========================================
# Task 5 - Seed
# ==========================================

np.random.seed(42)

print(np.random.randint(1,20,10))

# ==========================================
# Mini Challenge
# ==========================================

marks = np.random.randint(30,101,20)

print("Marks:", marks)
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Above 75:", marks[marks > 75])
```
