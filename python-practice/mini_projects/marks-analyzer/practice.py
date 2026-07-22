```python
import numpy as np

# Dataset
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 70],
    [88, 84, 91]
])

# ==========================================
# Shape Information
# ==========================================

students, subjects = marks.shape

print("Dataset Shape:", marks.shape)
print("Number of Students:", students)
print("Number of Subjects:", subjects)

# ==========================================
# Student Analysis
# ==========================================

student_avg = np.mean(marks, axis=1)

print("\nAverage Marks of Each Student")
print(student_avg)

print("\nTop Student Index:", np.argmax(student_avg))
print("Weakest Student Index:", np.argmin(student_avg))

# ==========================================
# Subject Analysis
# ==========================================

subject_avg = np.mean(marks, axis=0)

print("\nAverage Marks of Each Subject")
print(subject_avg)

print("\nHighest Marks in Each Subject")
print(np.max(marks, axis=0))

print("\nLowest Marks in Each Subject")
print(np.min(marks, axis=0))

# ==========================================
# Grace Marks
# ==========================================

grace = int(input("\nEnter Grace Marks: "))

updated_marks = marks + grace

print("\nUpdated Marks")
print(updated_marks)

# ==========================================
# Students Above 85 Average
# ==========================================

updated_avg = np.mean(updated_marks, axis=1)

print("\nStudents Scoring Above 85 Average")
print(updated_avg[updated_avg > 85])

print("Indices:", np.where(updated_avg > 85)[0])

# ==========================================
# Stretch Challenge
# ==========================================

subjects_name = np.array([
    "Maths",
    "Science",
    "English"
])

best_subject = np.argmax(subject_avg)

print("\nSubject with Highest Average:")
print(subjects_name[best_subject])
```
