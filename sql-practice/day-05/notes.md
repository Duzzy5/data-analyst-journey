# Day 05 - DISTINCT

## What is DISTINCT?

`DISTINCT` is used to return only unique values from a column or a combination of columns.

## Syntax

```sql
SELECT DISTINCT column_name
FROM table_name;
```

## Examples

### Display unique departments

```sql
SELECT DISTINCT department
FROM employees;
```

### Display unique ages

```sql
SELECT DISTINCT age
FROM employees;
```

### Display unique salary values

```sql
SELECT DISTINCT salary
FROM employees;
```

### Display unique combinations of department and age

```sql
SELECT DISTINCT department, age
FROM employees;
```

### Display unique departments in alphabetical order

```sql
SELECT DISTINCT department
FROM employees
ORDER BY department ASC;
```

## Key Points

* `DISTINCT` removes duplicate values.
* It can be used with one or multiple columns.
* When multiple columns are used, SQL checks the entire combination.
* `DISTINCT` can be combined with `ORDER BY`.

## Interview Tip

Use `DISTINCT` when you want to explore a dataset and find all unique values, such as departments, cities, categories, or job roles.
