# NumPy Syntax Reference - Day 1

```python
import numpy as np
```

Imports the NumPy library.

---

```python
np.array([1,2,3])
```

Creates a NumPy array from a Python list.

---

```python
np.zeros(5)
```

Creates an array of zeros.

---

```python
np.ones(5)
```

Creates an array of ones.

---

```python
np.full((3,3), 7)
```

Creates an array filled with a specific value.

---

```python
np.eye(3)
```

Creates a 3×3 identity matrix.

---

```python
np.arange(0,10,2)
```

Creates values using a fixed step size.

---

```python
np.linspace(0,1,5)
```

Creates a fixed number of equally spaced values.

---

```python
arr.shape
```

Returns the shape of the array.

---

```python
arr.ndim
```

Returns the number of dimensions.

---

```python
arr.size
```

Returns the total number of elements.

---

```python
arr.dtype
```

Returns the data type of the array.

---

```python
arr.itemsize
```

Returns the memory occupied by one element (bytes).

---

```python
arr.nbytes
```

Returns the total memory occupied by the array (bytes).

---

```python
arr.reshape(3,3)
```

Changes the shape of the array **without changing the data**.

**Rule:**

The total number of elements must remain the same.

Example:

```python
np.arange(1,10).reshape(3,3)
```

Output:

```text
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
