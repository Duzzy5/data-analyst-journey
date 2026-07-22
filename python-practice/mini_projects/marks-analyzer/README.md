# 📊 Marks Analyzer using NumPy

## Overview

This project analyzes the marks of students using NumPy without using loops. It demonstrates how multiple NumPy concepts can be combined to solve a real-world data analysis problem.

---

## Features

* Display dataset shape
* Count students and subjects
* Calculate average marks for each student
* Calculate average marks for each subject
* Find highest and lowest marks for every subject
* Apply grace marks using broadcasting
* Identify students scoring above a chosen average
* Find the top-performing student
* Find the weakest student
* Identify the subject with the highest average score

---

## NumPy Concepts Used

* ndarray
* shape
* Aggregation (`mean`, `max`, `min`)
* Axis (`axis=0`, `axis=1`)
* Broadcasting
* Boolean Indexing
* `np.where()`
* `np.argmax()`
* `np.argmin()`

---

## Project Structure

```text
marks-analyzer/
│
├── practice.py
├── learning.md
├── notes.md
└── README.md
```

---

## Sample Dataset

```python
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 70],
    [88, 84, 91]
])
```

---

## Learning Outcomes

After completing this project, I learned to:

* Analyze tabular data using NumPy.
* Work confidently with rows and columns using the `axis` parameter.
* Apply broadcasting instead of loops.
* Filter data using Boolean indexing.
* Use `argmax()` and `argmin()` to identify top and lowest performers.
* Combine multiple NumPy operations to solve a practical problem instead of using isolated functions.

---

## Future Improvements

* Read marks from a CSV file.
* Allow users to enter marks dynamically.
* Generate visualizations using Matplotlib.
* Convert the project into a Pandas version for larger datasets.

---

### Tech Stack

* Python 3
* NumPy

---

**Author:** Vibhav Keshar
