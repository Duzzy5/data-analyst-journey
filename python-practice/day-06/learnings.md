# NumPy Day 6 – Broadcasting

## Why Broadcasting?

Imagine a company wants to give every employee a ₹5000 bonus.

Without NumPy, you might loop through every salary.

With NumPy:

```python
salary + 5000
```

The operation is automatically applied to every element.

This feature is called **Broadcasting**.

---

## What is Broadcasting?

Broadcasting allows NumPy to perform arithmetic between arrays of compatible shapes without explicitly creating copies of the smaller array.

It makes code:

* Faster
* Shorter
* Easier to read

---

## Rule 1 – Scalars Always Broadcast

```python
arr + 5
arr - 2
arr * 10
arr / 4
```

The single value is applied to every element.

---

## Rule 2 – Same Shape

```python
a = np.array([1,2,3])
b = np.array([10,20,30])

a + b
```

Result:

```text
[11 22 33]
```

Operations occur element by element.

---

## Rule 3 – Compatible Shapes

```python
a.shape = (2,3)
b.shape = (3,)
```

NumPy treats `(3,)` as matching the columns and applies it to every row.

Example:

```python
marks + bonus
```

where

```python
bonus = np.array([5,2,3])
```

Each subject receives its own bonus.

---

## Rule 4 – Incompatible Shapes

```text
(2,3)

+

(2,)
```

This fails because the last dimensions (3 and 2) are different and neither is 1.

---

## Broadcasting Rules

NumPy compares dimensions from **right to left**.

Two dimensions are compatible if:

* They are equal.
* One of them is 1.

Otherwise, broadcasting fails.

---

## 2D Broadcasting

Example:

```python
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])

a + b
```

Shapes:

```text
(3,1)

(3,) → treated as (1,3)
```

Result shape:

```text
(3,3)
```

Output:

```text
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

---

## Real-World Applications

* Applying bonuses to salaries
* Increasing product prices
* Adding grace marks
* Currency conversion
* Scaling datasets

---

## Key Takeaways

* Always check the shapes first.
* Scalars always broadcast.
* Broadcasting avoids unnecessary loops.
* Compatible dimensions are equal or one of them is 1.
* NumPy performs broadcasting without physically duplicating memory.
