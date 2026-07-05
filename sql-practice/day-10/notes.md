# Day 10 - HAVING Clause

## What is HAVING?

The `HAVING` clause is used to filter groups after the `GROUP BY` clause has been applied.

Unlike `WHERE`, which filters individual rows, `HAVING` filters grouped results.

## Syntax

```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
GROUP BY column_name
HAVING AGGREGATE_FUNCTION(column_name) condition;
```

## Examples

### Departments having more than 2 employees

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
```

### Cities where the average salary is greater than ₹18,00,000

```sql
SELECT city, AVG(salary)
FROM employees
GROUP BY city
HAVING AVG(salary) > 1800000;
```

### Departments whose total salary is greater than ₹50,00,000

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department
HAVING SUM(salary) > 5000000;
```

## WHERE vs HAVING

| WHERE                          | HAVING                      |
| ------------------------------ | --------------------------- |
| Filters rows                   | Filters groups              |
| Used before `GROUP BY`         | Used after `GROUP BY`       |
| Cannot use aggregate functions | Can use aggregate functions |

## Key Points

* `HAVING` is used with `GROUP BY`.
* It filters groups based on aggregate functions.
* Common aggregate functions used with `HAVING` are `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()`.

## Interview Tip

If the business question contains words like **departments having**, **cities with**, or **groups where**, think of `HAVING` after `GROUP BY`.
