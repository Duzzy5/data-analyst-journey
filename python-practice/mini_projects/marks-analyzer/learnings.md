# Marks Analyzer – Learning Notes

## Project Goal

The objective of this project is to analyze student marks using NumPy without writing loops. It combines multiple NumPy concepts learned throughout the module.

Dataset:

```python
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 70],
    [88, 84, 91]
])
```

Each row represents a student.

Each column represents a subject.

---

# Concepts Used

## 1. Shape

```python
marks.shape
```

Returns the number of rows and columns.

Example:

```text
(5, 3)
```

Meaning:

* 5 Students
* 3 Subjects

---

## 2. Aggregation Functions

Used:

```python
np.mean()
np.max()
np.min()
```

### Student Average

```python
np.mean(marks, axis=1)
```

Calculates the average marks of every student.

### Subject Average

```python
np.mean(marks, axis=0)
```

Calculates the average marks of every subject.

---

## 3. Axis Concept

```text
axis = 0 → Columns (Subjects)

axis = 1 → Rows (Students)
```

This project heavily relies on choosing the correct axis.

---

## 4. Broadcasting

Grace marks are added without loops.

```python
marks = marks + 5
```

NumPy automatically adds 5 to every element.

---

## 5. Boolean Indexing

Find students whose average is above a threshold.

```python
student_avg = np.mean(marks, axis=1)

student_avg[student_avg > 85]
```

---

## 6. argmax() and argmin()

These functions return indices, not values.

```python
np.argmax(student_avg)
```

Returns the index of the student with the highest average.

```python
np.argmin(student_avg)
```

Returns the index of the student with the lowest average.

---

# What I Learned

* Choosing the correct axis is more important than memorizing functions.
* Broadcasting replaces loops for many operations.
* Boolean indexing filters data efficiently.
* argmax() and argmin() return positions instead of values.
* Real-world data analysis combines multiple NumPy operations together rather than using isolated functions.
