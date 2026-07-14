# NumPy Day 8 – Random Module

# Why Random Numbers?

Random numbers are used throughout Data Science and Machine Learning.

Examples include:

* Generating sample datasets
* Initializing machine learning models
* Splitting data into train and test sets
* Simulations
* Games
* Statistical experiments

NumPy provides a fast and flexible random module for these tasks.

---

# Random Integers

Generate one random integer.

```python
np.random.randint(1, 10)
```

Returns a value between **1 and 9**.

The upper limit is excluded.

Generate multiple integers.

```python
np.random.randint(1, 10, size=5)
```

Example Output

```text
[3 7 1 9 5]
```

---

# Random Floats

Generate one random float.

```python
np.random.rand()
```

Returns a floating-point value between **0 and 1**.

Generate multiple values.

```python
np.random.rand(5)
```

Generate a matrix.

```python
np.random.rand(3,3)
```

Returns a 3×3 matrix of random floating-point numbers.

---

# Random Choice

Randomly select values from an array.

```python
colors = np.array(["Red","Blue","Green"])

np.random.choice(colors)
```

Randomly choose multiple values.

```python
np.random.choice(colors, size=3)
```

---

# Shuffle

Shuffle rearranges the elements of an existing array.

```python
np.random.shuffle(arr)
```

Unlike many NumPy functions, **shuffle modifies the original array**.

---

# Random Seed

Random values usually change every time the program runs.

To generate the same random values repeatedly, use:

```python
np.random.seed(42)
```

This makes experiments reproducible.

Machine Learning projects frequently use a fixed seed.

---

# Real World Applications

* Creating dummy datasets
* Simulating customer behaviour
* Cross-validation
* Model initialization
* Reproducible experiments

---

# Key Takeaways

* randint() generates random integers.
* rand() generates random floating-point numbers.
* choice() randomly selects values.
* shuffle() changes the original array.
* seed() ensures reproducible results.
