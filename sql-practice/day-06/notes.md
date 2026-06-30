# Day 06 - Aliases (AS)

## What is an Alias?

An alias is a temporary name given to a column or an expression in the query result. It improves readability without changing the actual table.

## Syntax

```sql
SELECT column_name AS alias_name
FROM table_name;
```

## Examples

### Rename a column

```sql
SELECT name AS Employee_Name
FROM employees;
```

### Rename multiple columns

```sql
SELECT
    department AS Department_Name,
    salary AS Monthly_Salary
FROM employees;
```

### Alias with a calculated column

```sql
SELECT
    name,
    salary,
    salary * 12 AS Annual_Salary
FROM employees;
```

## Key Points

* Aliases change only the output, not the table.
* `AS` is optional but recommended for better readability.
* Aliases can be used with calculated expressions.
* Good aliases make reports easier to understand.

## Interview Tip

Write SQL for humans, not just databases. Clear column names make reports professional and easier to read.
