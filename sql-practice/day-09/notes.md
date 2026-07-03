# Day 09 - GROUP BY

## What is GROUP BY?

`GROUP BY` is used to group rows that have the same values in one or more columns. It is commonly used with aggregate functions to calculate summaries for each group.

## Syntax

```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
GROUP BY column_name;
```

## Examples

### Count employees in each department

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

### Average salary in each department

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

### Highest salary in each department

```sql
SELECT department, MAX(salary)
FROM employees
GROUP BY department;
```

### Count employees in each city

```sql
SELECT city, COUNT(*)
FROM employees
GROUP BY city;
```

### Total salary in each department

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

## Key Points

* `GROUP BY` groups similar rows together.
* It is mostly used with aggregate functions.
* Think of words like **each**, **every**, **per**, or **by** as hints to use `GROUP BY`.
* SQL first creates the groups and then performs the aggregate calculation on each group.

## Interview Tip

Whenever you hear:

* Average salary **per department**
* Employees **in each city**
* Total sales **by category**

Immediately think: **GROUP BY**
