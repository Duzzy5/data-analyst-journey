# NumPy Day 4 - Quick Revision

## Vectorization

Perform one operation on the entire array without writing loops.

---

## Universal Functions (ufuncs)

Optimized NumPy functions that work element-by-element.

Examples:

* np.abs()
* np.sqrt()
* np.square()
* np.max()
* np.min()
* np.sum()
* np.mean()

---

## Array Arithmetic

```python
arr + 5
arr - 5
arr * 2
arr / 2
arr ** 2
arr % 2
```

---

## Array vs Array

```python
a + b
a - b
a * b
a / b
```

These perform **element-wise operations**.

---

## Important Interview Points

* NumPy is faster because it uses vectorization, contiguous memory and optimized C code.
* `a * b` is **element-wise multiplication**, not matrix multiplication.
* Universal Functions eliminate the need for explicit loops in many numerical tasks.

---

## Formulas

Average

```text
mean = sum of all elements / total number of elements
```

Memory

```text
nbytes = size × itemsize
```

---

## Remember

Whenever you think,

> "I should write a loop..."

Ask yourself,

> "Can NumPy do this directly?"
