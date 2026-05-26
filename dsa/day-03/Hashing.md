# Hashing

## What is Hashing?

Hashing means:

> Store useful information so searching becomes fast.

Mostly used for:
- frequency counting
- duplicate detection
- fast lookup
- storing visited elements

---

# Python Structures Used in Hashing

## Dictionary

```python
d = {}
```

Stores:

```python
key : value
```

Example:

```python
{
 1:3,
 2:2
}
```

Meaning:

```python
1 appears 3 times
2 appears 2 times
```

---

## Set

```python
s = set()
```

Stores only unique elements.

Example:

```python
{1,2,3}
```

Used for:
- duplicates
- fast searching
- visited elements

---

# Most Important Hashing Pattern

```python
d = {}

for i in arr:

    if i in d:
        d[i] += 1

    else:
        d[i] = 1
```

Meaning:

```python
element → frequency
```

---

# Important Concepts

## Fast Lookup

```python
if i in s
```

means:

```python
Check whether i already exists
```

Hashing makes this fast.

---

# Dictionary vs Set

## Dictionary

Used when we need:

```python
value associated with something
```

Example:

```python
1 → 3 times
```

---

## Set

Used when we only care:

```python
Exists or not?
```

---

# Big Hashing Mindset

Hashing means:

```python
Store useful information while traversing
```

---

# Questions Practiced

1. Frequency Count
2. Duplicate Detection
3. First Duplicate
4. Count Unique Elements
5. Highest Frequency Element
6. Character Frequency
7. Most Frequent Character
8. Common Element Between Two Arrays

---

# Important Syntax

## Frequency Map

```python
d[i] += 1
```

means:

```python
increase frequency
```

---

## Highest Frequency

```python
max(d.values())
```

Gives:

```python
highest frequency value
```

---

## Element with Highest Frequency

```python
max(d, key=d.get)
```

Gives:

```python
element having maximum frequency
```

---

# Real Essence of Hashing

Without hashing:

```python
search again and again
```

With hashing:

```python
store once → use many times
```
