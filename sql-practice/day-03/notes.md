# Day 03 - ORDER BY

## What is ORDER BY?

`ORDER BY` is used to sort the rows returned by a query.

## Syntax

```sql
SELECT column_name
FROM table_name
ORDER BY column_name;
```

## Sorting Order

* `ASC` → Ascending Order (Default)
* `DESC` → Descending Order

### Examples

Sort salary from lowest to highest:

```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

Sort salary from highest to lowest:

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

Sort employee names alphabetically:

```sql
SELECT *
FROM employees
ORDER BY name ASC;
```

## Key Points

* `SELECT` chooses the columns.
* `WHERE` filters the rows.
* `ORDER BY` sorts the rows.
* If `ASC` or `DESC` is not specified, SQL uses `ASC` by default.
* `ORDER BY` can be used on numeric as well as text columns.

## Interview Tip

Think in this order:

**Business Requirement → SELECT → WHERE (if needed) → ORDER BY**
