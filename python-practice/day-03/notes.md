# NumPy Day 3 - Boolean Indexing, Conditional Filtering & Fancy Indexing

# Why Boolean Indexing?

In data analysis, we rarely need the entire dataset.

Instead, we ask questions like:

* Which students scored above 80?
* Which employees earn more than ₹50,000?
* Which products are out of stock?

Boolean Indexing allows us to answer these questions without writing loops.

---

# Boolean Comparisons

NumPy compares every element in an array individually.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr > 25)
```

Output:

```text
[False False True True True]
```

Each element is checked independently.

---

# Boolean Masks

The boolean array created after a comparison is called a **Boolean Mask**.

Example:

```python
arr > 25
```

creates

```text
[False False True True True]
```

NumPy then uses this mask to select only the `True` values.

Example:

```python
arr[arr > 25]
```

Output:

```text
[30 40 50]
```

---

# Conditional Filtering

Boolean masks allow us to filter data quickly.

Example:

```python
marks = np.array([45, 67, 89, 90, 34, 76, 58, 99])

marks[marks > 75]
```

Output:

```text
[89 90 76 99]
```

No loops are required.

---

# Multiple Conditions

Python's `and` and `or` do not work with NumPy arrays because they expect a single boolean value.

Instead, NumPy provides element-wise logical operators.

AND

```python
(marks > 60) & (marks < 90)
```

OR

```python
(marks < 40) | (marks > 90)
```

Always wrap each condition inside parentheses.

---

# Fancy Indexing

Fancy Indexing selects specific elements or rows using a list of indices.

Example:

```python
arr = np.array([10,20,30,40,50])

arr[[0,2,4]]
```

Output:

```text
[10 30 50]
```

---

# Fancy Indexing in 2D Arrays

```python
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

arr[[0,3]]
```

Output:

```text
[[1 2]
 [7 8]]
```

Rows are selected by index.

---

# Real World Applications

Boolean Indexing is used for:

* Filtering customers
* Selecting high-performing students
* Finding employees above a salary threshold
* Removing invalid values
* Cleaning datasets before machine learning

Fancy Indexing is useful for selecting specific rows, samples or features.

---

# Key Takeaways

* Comparisons are performed element-by-element.
* Boolean comparisons create a Boolean Mask.
* Boolean Masks are used for filtering.
* Use `&` for AND and `|` for OR.
* Parentheses are required around each condition.
* Fancy Indexing uses a list of indices.
* `arr[2]` returns a scalar, while `arr[[2]]` returns a NumPy array.
