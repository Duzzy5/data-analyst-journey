# Day 08 - Aggregate Functions

## What are Aggregate Functions?

Aggregate functions perform calculations on multiple rows and return a single summarized value.

## Common Aggregate Functions

### COUNT()

Returns the total number of rows.

```sql
SELECT COUNT(*)
FROM employees;
```

### SUM()

Returns the total of a numeric column.

```sql
SELECT SUM(salary)
FROM employees;
```

### AVG()

Returns the average value of a numeric column.

```sql
SELECT AVG(salary)
FROM employees;
```

### MAX()

Returns the highest value.

```sql
SELECT MAX(salary)
FROM employees;
```

### MIN()

Returns the lowest value.

```sql
SELECT MIN(salary)
FROM employees;
```

## Key Points

* Aggregate functions summarize data.
* They return a single value.
* They are commonly used for reports and business insights.
* They are usually applied to numeric columns, except `COUNT()` which can count rows.

## Interview Tip

Ask yourself:

**"Does the business need individual records or a summary?"**

If the answer is **summary**, think of aggregate functions.
