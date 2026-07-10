# NumPy Day 3 - Quick Revision

## Boolean Comparison

```python
arr > 10
arr < 20
arr >= 30
arr <= 40
arr == 25
arr != 50
```

Returns a Boolean array.

---

## Boolean Indexing

```python
arr[arr > 20]
```

Returns only the elements that satisfy the condition.

---

## Multiple Conditions

AND

```python
(arr > 20) & (arr < 50)
```

OR

```python
(arr < 20) | (arr > 50)
```

Remember:

* Use `&` instead of `and`
* Use `|` instead of `or`
* Always use parentheses around each condition

---

## Even Numbers

```python
arr[arr % 2 == 0]
```

---

## Fancy Indexing (1D)

```python
arr[[0,2,4]]
```

Selects elements at indices 0, 2 and 4.

---

## Fancy Indexing (2D)

```python
arr[[0,3]]
```

Selects the first and fourth rows.

---

## Important Interview Points

* `and` and `or` do not work on NumPy arrays.
* `&` and `|` perform element-wise logical operations.
* `arr[2]` returns a scalar.
* `arr[[2]]` returns an ndarray.
* Boolean Indexing is one of the most frequently used techniques in data analysis.

---

## Remember

Whenever you need to filter data, think:

> "Can I create a Boolean Mask?"

Example:

```python
arr[arr > 25]
```

Output:

```text
[30 40 50]
```

---

# Conditional Filtering

Boolean masks allow us to filter data quickly.

Example:

```python
marks = np.array([45, 67, 89, 90, 34, 76, 58, 99])

marks[marks > 75]
```

Output:

```text
[89 90 76 99]
```

No loops are required.

---

# Multiple Conditions

Python's `and` and `or` do not work with NumPy arrays because they expect a single boolean value.

Instead, NumPy provides element-wise logical operators.

AND

```python
(marks > 60) & (marks < 90)
```

OR

```python
(marks < 40) | (marks > 90)
```

Always wrap each condition inside parentheses.

---

# Fancy Indexing

Fancy Indexing selects specific elements or rows using a list of indices.

Example:

```python
arr = np.array([10,20,30,40,50])

arr[[0,2,4]]
```

Output:

```text
[10 30 50]
```

---

# Fancy Indexing in 2D Arrays

```python
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

arr[[0,3]]
```

Output:

```text
[[1 2]
 [7 8]]
```

Rows are selected by index.

---

# Real World Applications

Boolean Indexing is used for:

* Filtering customers
* Selecting high-performing students
* Finding employees above a salary threshold
* Removing invalid values
* Cleaning datasets before machine learning

Fancy Indexing is useful for selecting specific rows, samples or features.

---

# Key Takeaways

* Comparisons are performed element-by-element.
* Boolean comparisons create a Boolean Mask.
* Boolean Masks are used for filtering.
* Use `&` for AND and `|` for OR.
* Parentheses are required around each condition.
* Fancy Indexing uses a list of indices.
* `arr[2]` returns a scalar, while `arr[[2]]` returns a NumPy array.
