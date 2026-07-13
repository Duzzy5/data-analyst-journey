# NumPy Day 7 – Sorting, Searching & Unique Values

# Why Sorting?

Sorting helps organize data for analysis.

Examples:

* Highest salary
* Lowest marks
* Top-selling products
* Alphabetical categories

NumPy provides fast built-in sorting functions.

---

# Sorting

Ascending order

```python
np.sort(arr)
```

Returns a new sorted array.

The original array remains unchanged.

Descending order

```python
np.sort(arr)[::-1]
```

Uses slicing to reverse the sorted array.

---

# Sorting 2D Arrays

Row-wise (default)

```python
np.sort(arr)
```

Each row is sorted independently.

Column-wise

```python
np.sort(arr, axis=0)
```

Each column is sorted independently.

---

# Unique Values

```python
np.unique(arr)
```

Returns only distinct values.

Useful for:

* Categories
* Labels
* Departments
* Cities

---

# Frequency Count

```python
np.unique(arr, return_counts=True)
```

Returns:

* Unique values
* Number of occurrences of each value

Useful for quick frequency analysis.

---

# Searching with np.where()

```python
np.where(arr == value)
```

Returns the indices where the condition is satisfied.

Example

```python
np.where(arr == 20)
```

Output

```text
(array([1,3]),)
```

---

# Difference Between np.where() and Boolean Indexing

```python
np.where(arr > 50)
```

Returns indices.

```python
arr[arr > 50]
```

Returns values.

---

# Real-World Applications

* Finding duplicate records
* Counting categories
* Searching specific values
* Ranking data
* Preparing datasets before visualization

---

# Key Takeaways

* np.sort() returns a new sorted array.
* np.unique() removes duplicates and returns sorted unique values.
* return_counts=True provides frequencies.
* np.where() returns indices.
* Boolean Indexing returns values.
