# NumPy Day 9 – Linear Algebra Basics

## Why Linear Algebra?

Linear Algebra is the mathematical language behind Machine Learning.

Every ML algorithm internally performs operations on vectors and matrices.

Examples:

* Linear Regression
* Logistic Regression
* Neural Networks
* PCA
* Recommendation Systems

For Data Analysis, you only need the core concepts.

---

## Transpose

The transpose of a matrix swaps rows and columns.

```python
arr.T
```

Example:

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])
```

Shape:

```text
(2,3)
```

After transpose:

```text
1 4
2 5
3 6
```

New Shape:

```text
(3,2)
```

---

## Dot Product

```python
np.dot(a,b)
```

For vectors:

Each element is multiplied with the corresponding element, and all products are added together.

Example:

```text
1×4 + 2×5 + 3×6 = 32
```

The result is a single number.

---

## Matrix Multiplication

Element-wise multiplication:

```python
a * b
```

Matrix multiplication:

```python
a @ b
```

or

```python
np.matmul(a,b)
```

These are completely different operations.

---

## Identity Matrix

```python
np.eye(n)
```

Creates a square matrix with:

* Diagonal = 1
* Everything else = 0

It behaves like the number **1** for matrix multiplication.

```text
A @ I = A
```

---

## Matrix Inverse

```python
np.linalg.inv(A)
```

Returns the inverse of a square matrix.

Widely used in statistics and machine learning.

---

## Key Takeaways

* `.T` swaps rows and columns.
* `*` performs element-wise multiplication.
* `@` performs matrix multiplication.
* `np.dot()` computes the dot product.
* `np.eye()` creates an identity matrix.
* `np.linalg.inv()` calculates the matrix inverse.
