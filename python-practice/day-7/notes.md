# NumPy Day 7 - Quick Revision

## Sorting

```python
np.sort(arr)
```

Ascending order.

---

```python
np.sort(arr)[::-1]
```

Descending order.

---

## Sort Along Axis

```python
np.sort(arr)
```

Sort each row.

```python
np.sort(arr, axis=0)
```

Sort each column.

---

## Unique Values

```python
np.unique(arr)
```

Returns sorted unique values.

---

## Frequency Count

```python
np.unique(arr, return_counts=True)
```

Returns:

* Unique values
* Counts

---

## Searching

```python
np.where(condition)
```

Returns indices.

---

## Boolean Indexing

```python
arr[condition]
```

Returns values.

---

# Interview Points

* np.sort() does not modify the original array.
* np.unique() automatically sorts unique values.
* np.where() returns indices, not values.
* Boolean Indexing returns matching values directly.
