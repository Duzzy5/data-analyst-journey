# ===============================

# NumPy Day 2 Syntax

# ===============================

```python
arr[index]
```

Returns the element at the given index.

---

```python
arr[-1]
```

Returns the last element.

---

```python
arr[start:stop]
```

Returns elements from start to stop (stop excluded).

---

```python
arr[start:stop:step]
```

Returns elements using a custom step size.

---

```python
arr[::-1]
```

Returns the array in reverse order.

---

```python
arr[row, column]
```

Accesses a specific element from a 2D array.

---

```python
arr[row, :]
```

Returns the complete row.

---

```python
arr[:, column]
```

Returns the complete column.

---

```python
arr[row_start:row_stop, column_start:column_stop]
```

Returns a submatrix.

---

```python
arr[:, ::2]
```

Returns every second column.

---

```python
arr[::2]
```

Returns every second row.

---

```python
arr.reshape(rows, columns)
```

Changes the dimensions of the array.

Rule

```
rows × columns = total number of elements
```

---

```python
np.arange(12).reshape(3,4)
```

Creates a 1D array and immediately reshapes it into a 3×4 matrix.
