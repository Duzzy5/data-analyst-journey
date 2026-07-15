# NumPy Day 9 – Quick Revision

## Transpose

```python
arr.T
```

Rows become columns.

---

## Dot Product

```python
np.dot(a,b)
```

Returns a single weighted value.

---

## Matrix Multiplication

```python
a @ b
```

or

```python
np.matmul(a,b)
```

---

## Element-wise Multiplication

```python
a * b
```

Different from matrix multiplication.

---

## Identity Matrix

```python
np.eye(4)
```

Diagonal = 1

Others = 0

---

## Matrix Inverse

```python
np.linalg.inv(A)
```

Returns the inverse of a square matrix.

---

## Interview Points

* `*` → Element-wise multiplication.
* `@` → Matrix multiplication.
* `.T` → Transpose.
* `(A.T).T = A`
* Identity Matrix behaves like 1 in matrix multiplication.
