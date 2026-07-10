# NumPy Day 4 - Vectorization & Universal Functions

# Why was Vectorization invented?

Imagine you have the salaries of 10 million employees.

In normal Python, if you want to give everyone a ₹5000 bonus, you would usually write a loop that updates one salary at a time.

NumPy takes a different approach.

Instead of telling Python **how** to process each element, you tell NumPy **what** operation you want.

Example:

```python
salary + 5000
```

NumPy automatically applies the operation to every element in the array.

This is called **Vectorization**.

Because NumPy performs these operations using optimized C code on contiguous memory, it is significantly faster than Python loops.

---

# Universal Functions (ufuncs)

Universal Functions are optimized mathematical functions that operate element-by-element on NumPy arrays.

Examples include:

* Addition
* Subtraction
* Multiplication
* Division
* Square Root
* Absolute Value
* Maximum
* Minimum
* Sum
* Mean

---

# Array Arithmetic

NumPy performs arithmetic on every element automatically.

Example:

```python
arr = np.array([10,20,30])

arr + 5
```

Output:

```text
[15 25 35]
```

The same applies to subtraction, multiplication, division, powers and modulus.

---

# Element-wise Operations

When two arrays have the same shape, NumPy performs operations element-by-element.

Example:

```python
a = np.array([1,2,3])

b = np.array([10,20,30])

a + b
```

Output:

```text
[11 22 33]
```

Example:

```python
a * b
```

Output:

```text
[10 40 90]
```

This is **not** matrix multiplication.

---

# Important Mathematical Functions

```python
np.abs()
```

Returns absolute values.

```python
np.sqrt()
```

Returns square roots.

```python
np.square()
```

Squares every element.

```python
np.max()
```

Returns the maximum value.

```python
np.min()
```

Returns the minimum value.

```python
np.sum()
```

Returns the total sum.

```python
np.mean()
```

Returns the average.

---

# Real World Applications

Data Analysts frequently use vectorization to:

* Apply discounts
* Increase salaries
* Convert currencies
* Normalize data
* Scale values
* Perform statistical calculations

Using loops for these operations is slower and less readable.

---

# Key Takeaways

* Think in terms of entire arrays, not individual elements.
* Prefer vectorized operations over loops whenever possible.
* Universal Functions are optimized for speed and readability.
* Arithmetic between arrays is element-wise by default.
* Matrix multiplication is a different operation.
