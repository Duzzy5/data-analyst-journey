# NumPy Day 6 – Quick Revision

## Broadcasting

Perform operations between arrays of compatible shapes.

---

## Scalar Broadcasting

```python
arr + 10
arr * 2
arr / 5
```

---

## Same Shape

```python
a + b
a - b
a * b
a / b
```

Element-wise operations.

---

## Broadcasting Rule

Compare shapes from **right to left**.

Compatible if:

* Same dimension
* One dimension is 1

Otherwise:

```text
ValueError
```

---

## Examples

```text
(3,) + (3,)   ✅

(2,3) + (3,)  ✅

(2,3) + (2,)  ❌

(3,1) + (3,)  ✅
```

---

## Interview Points

* Broadcasting avoids explicit loops.
* Broadcasting does not create duplicate arrays in memory.
* Broadcasting works only for compatible shapes.

---

## Memory Trick

Before every operation, ask:

> **What are the shapes?**
