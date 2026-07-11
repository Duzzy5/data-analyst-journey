# NumPy Day 5 - Quick Revision

## Aggregation Functions

```python
np.sum(arr)
```

Returns total.

---

```python
np.mean(arr)
```

Returns average.

---

```python
np.max(arr)
```

Largest value.

---

```python
np.min(arr)
```

Smallest value.

---

```python
np.median(arr)
```

Middle value after sorting.

---

```python
np.std(arr)
```

Standard Deviation.

---

```python
np.var(arr)
```

Variance.

---

# Axis

## axis = 0

Rows collapse.

Columns remain.

One result per column.

Example

```python
np.sum(arr, axis=0)
```

---

## axis = 1

Columns collapse.

Rows remain.

One result per row.

Example

```python
np.mean(arr, axis=1)
```

---

# Memory Trick

```text
axis = 0
↓

Columns survive

axis = 1
→

Rows survive
```

---

# Real World Mapping

Student Average

↓

axis = 1

Subject Average

↓

axis = 0

---

# Interview Points

* Aggregation converts many values into one meaningful summary.
* `np.sum(arr)` aggregates the whole array.
* `np.sum(arr, axis=0)` aggregates each column.
* `np.sum(arr, axis=1)` aggregates each row.

---

# Formula

Average

```text
Mean = Sum / Number of Elements
```
