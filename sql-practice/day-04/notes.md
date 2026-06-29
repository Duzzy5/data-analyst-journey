# Day 04 - LIMIT

## What is LIMIT?

The `LIMIT` clause is used to restrict the number of rows returned by a query.

## Syntax

```sql
SELECT column_name
FROM table_name
LIMIT number;
```

## Examples

### Show first 3 employees

```sql
SELECT *
FROM employees
LIMIT 3;
```

### Show the highest-paid employee

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

### Show the top 2 highest-paid employees

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 2;
```

## Key Points

* `LIMIT` restricts the number of rows returned.
* It is commonly used with `ORDER BY` to get Top N or Bottom N records.
* `ORDER BY` executes before `LIMIT`.
* `LIMIT` can also be used without `ORDER BY`.

## Interview Tip

Think in this order:

**Business Requirement → SELECT → WHERE (if needed) → ORDER BY (if needed) → LIMIT**
