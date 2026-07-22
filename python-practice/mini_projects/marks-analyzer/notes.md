# Marks Analyzer – Quick Revision

## Shape

```python
marks.shape
```

Returns:

```text
(rows, columns)
```

---

## Student Average

```python
np.mean(marks, axis=1)
```

---

## Subject Average

```python
np.mean(marks, axis=0)
```

---

## Highest Subject Marks

```python
np.max(marks, axis=0)
```

---

## Lowest Subject Marks

```python
np.min(marks, axis=0)
```

---

## Broadcasting

```python
marks = marks + 5
```

Adds 5 to every element.

---

## Boolean Indexing

```python
avg = np.mean(marks, axis=1)

avg[avg > 85]
```

---

## argmax()

```python
np.argmax(avg)
```

Returns the index of the highest value.

---

## argmin()

```python
np.argmin(avg)
```

Returns the index of the lowest value.

---

# Interview Points

* `axis=0` → Columns
* `axis=1` → Rows
* `argmax()` returns an index, not a value.
* `argmin()` returns an index, not a value.
* Broadcasting eliminates the need for loops.
