
# NumPy Day 5 - Aggregation & Axis

# Why do we need Aggregation?

Imagine you work as a Data Analyst in a company.

The CEO does not want to see thousands of numbers.

Instead, they ask questions like:

* What are the total sales?
* What is the average salary?
* Which department has the highest revenue?
* Which student scored the highest?

Notice something.

They don't ask for every individual value.

They ask for a **summary**.

The process of converting many values into one meaningful value is called **Aggregation**.

---

# Common Aggregation Functions

## Sum

Returns the total of all elements.

```python
np.sum(arr)
```

Example

```python
arr = np.array([10,20,30])

np.sum(arr)
```

Output

```text
60
```

---

## Mean

Returns the average value.

Formula

Average = Sum / Number of Elements

```python
np.mean(arr)
```

---

## Maximum

Returns the largest value.

```python
np.max(arr)
```

---

## Minimum

Returns the smallest value.

```python
np.min(arr)
```

---

## Median

Median is the middle value after sorting.

Example

```python
arr = np.array([50,10,30])

np.median(arr)
```

Sorted Array

```text
10 30 50
```

Median

```text
30
```

---

## Standard Deviation

```python
np.std(arr)
```

Standard deviation measures how spread out the data is.

Small Standard Deviation

↓

Values are close together.

Large Standard Deviation

↓

Values are spread apart.

(We'll study the mathematics in Statistics.)

---

## Variance

```python
np.var(arr)
```

Variance is another measure of spread.

Again, only remember the syntax for now.

---

# Understanding Axis

This is one of the most confusing topics for beginners.

Let's understand it visually.

Suppose

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
```

Shape

```text
(3,3)
```

---

## axis = 0

Think of Axis 0 as moving vertically.

```text
10
40
70
```

These values combine into one result.

Then

```text
20
50
80
```

combine.

Then

```text
30
60
90
```

combine.

Example

```python
np.sum(arr, axis=0)
```

Output

```text
[120 150 180]
```

Rows disappear.

Columns remain.

Result:

One value for every column.

---

## axis = 1

Now move horizontally.

```text
10 20 30
```

becomes

```text
60
```

Then

```text
40 50 60
```

becomes

```text
150
```

Example

```python
np.sum(arr, axis=1)
```

Output

```text
[60 150 240]
```

Columns disappear.

Rows remain.

Result:

One value for every row.

---

# Real World Example

Suppose every row is a student.

```text
Math Science English

85   90      95

70   65      80

95   92      98
```

Average marks of each student

↓

Use

```python
axis=1
```

Average marks of each subject

↓

Use

```python
axis=0
```

Always ask yourself:

> Am I summarizing rows or columns?

---

# Common Mistakes

❌ Thinking axis = 0 means rows.

Actually,

axis = 0 performs calculations down the rows and returns one value per column.

---

❌ Forgetting what disappears.

Remember

axis = 0

↓

Rows disappear.

axis = 1

↓

Columns disappear.

---

# Interview Tips

Difference between

```python
np.sum(arr)
```

and

```python
np.sum(arr, axis=0)
```

Answer:

The first returns the sum of every element in the array.

The second returns one sum for each column.

---

# Key Takeaways

* Aggregation summarizes data.
* Sum, Mean, Max, Min, Median, Standard Deviation and Variance are the most commonly used aggregation functions.
* axis=0 returns one result for each column.
* axis=1 returns one result for each row.
* Visualize the matrix instead of memorizing the axis values.
