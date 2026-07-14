# NumPy Day 8 – Quick Revision

## Random Integer

```python
np.random.randint(low, high)
```

One integer.

```python
np.random.randint(low, high, size=n)
```

Multiple integers.

---

## Random Float

```python
np.random.rand()
```

One float between 0 and 1.

```python
np.random.rand(3,3)
```

Random matrix.

---

## Random Choice

```python
np.random.choice(arr)
```

One random element.

```python
np.random.choice(arr, size=3)
```

Multiple random elements.

---

## Shuffle

```python
np.random.shuffle(arr)
```

Shuffles the original array.

---

## Seed

```python
np.random.seed(42)
```

Produces the same random output every time.

---

# Interview Points

* randint() → Random integers.
* rand() → Random floating-point values.
* shuffle() modifies the original array.
* seed() makes experiments reproducible.
