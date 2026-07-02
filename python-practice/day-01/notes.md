# NumPy Day 1 Notes

# Why NumPy?

NumPy (Numerical Python) is a library used for fast numerical computation.

Unlike Python lists, NumPy stores elements of the same data type in one continuous block of memory, making operations much faster and more memory efficient.

---

# ndarray

The core object in NumPy is the **ndarray (N-dimensional Array)**.

It can represent:

* 1D arrays (vectors)
* 2D arrays (matrices)
* 3D arrays and higher-dimensional data

Example:

```python
arr = np.array([1, 2, 3])
```

---

# Array Creation Functions

## np.array()

Creates an array from a Python list.

## np.zeros(shape)

Creates an array filled with zeros.

## np.ones(shape)

Creates an array filled with ones.

## np.eye(n)

Creates an identity matrix.

## np.arange(start, stop, step)

Creates evenly spaced values using a fixed step size.

Example:

```python
np.arange(0, 10, 2)
# Output:
# [0 2 4 6 8]
```

If the step is omitted, NumPy uses a default step of **1**.

## np.linspace(start, stop, num)

Creates a specified number of equally spaced values between two numbers.

Example:

```python
np.linspace(0, 1, 5)
# Output:
# [0.   0.25 0.5  0.75 1. ]
```

---

# Array Attributes

## shape

Returns the size along each dimension.

Example:

```python
(3, 4)
```

means 3 rows and 4 columns.

---

## ndim

Returns the number of dimensions (axes).

Examples:

* (5,) → 1D
* (3,4) → 2D
* (2,3,4) → 3D

---

## size

Returns the total number of elements.

Formula:

size = product of all values in shape

---

## dtype

Returns the data type of the array.

Common dtypes:

* int16
* int32
* int64
* float32
* float64
* bool

---

## itemsize

Memory occupied by one element (in bytes).

Examples:

* int16 → 2 bytes
* int32 → 4 bytes
* int64 → 8 bytes
* float64 → 8 bytes

---

## nbytes

Total memory occupied by the entire array.

Formula:

nbytes = size × itemsize

---

# Homogeneous Data

NumPy arrays store only one data type.

This allows:

* Faster computation
* Better memory efficiency
* Vectorized operations

---

# Key Takeaways

* NumPy is designed for fast numerical computing.
* ndarray is the fundamental NumPy object.
* shape tells the dimensions of the array.
* size tells the total number of elements.
* itemsize tells memory per element.
* nbytes tells total memory usage.
* arange() uses a step size.
* linspace() uses the number of values.
