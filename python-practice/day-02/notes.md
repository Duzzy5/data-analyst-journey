# NumPy Day 2 — Indexing, Slicing & Reshape

---

# Indexing

Indexing allows us to access individual elements of an array.

## 1D Indexing

```python
arr = np.array([10,20,30,40])

arr[0]
```

Output:

```
10
```

Negative indexing starts from the end.

```python
arr[-1]
```

Output:

```
40
```

---

# 2D Indexing

General Syntax

```python
arr[row, column]
```

Example

```python
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr[2,1]
```

Output

```
8
```

---

# Slicing

General Syntax

```python
arr[start:stop:step]
```

Rules

* start is included.
* stop is excluded.
* step defaults to 1.

Example

```python
arr[1:4]
```

Output

```
20 30 40
```

---

# Negative Slicing

Reverse an array

```python
arr[::-1]
```

Example Output

```
50 40 30 20 10
```

---

# 2D Slicing

General Syntax

```python
arr[rows, columns]
```

Examples

Entire first row

```python
arr[0,:]
```

Entire first column

```python
arr[:,0]
```

Top-left 2×2 matrix

```python
arr[0:2,0:2]
```

---

# Understanding Row and Column Selection

```
arr[row_slice, column_slice]
```

Examples

```
arr[:,1]
```

means

* All rows
* Second column

```
arr[1,:]
```

means

* Second row
* All columns

---

# Step in 2D Slicing

Rows can also have a step.

```python
arr[::2]
```

Selects every second row.

Columns can also have a step.

```python
arr[:,::2]
```

Selects every second column.

Both together

```python
arr[1:4:2, ::2]
```

means

* Rows 1 to 3 with a step of 2.
* Every second column.

---

# Reshape

Reshape changes the dimensions of an array without changing its data.

Example

```python
arr = np.arange(12)

arr.reshape(3,4)
```

Important Rule

The total number of elements must remain the same.

Valid

```
12 elements

3 × 4

2 × 6

1 × 12
```

Invalid

```
12 elements

5 × 5
```

because 25 ≠ 12.

---

# Key Takeaways

* Indexing accesses one element.
* Slicing accesses multiple elements.
* Negative indexing starts from the end.
* 2D arrays use row and column indexing.
* Rows and columns can both have step values.
* reshape() only changes the structure, not the data.
* reshape() never creates or removes elements.
