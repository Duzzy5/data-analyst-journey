# Day 02 - WHERE Clause

## What is the WHERE Clause?

The WHERE clause is used to filter rows based on a condition. Instead of returning every row in a table, it returns only the rows that satisfy the given condition.

## Syntax

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| = | Equal to |
| != | Not Equal to |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

## Examples

### Employees older than 21

```sql
SELECT *
FROM employees
WHERE age > 21;
```

### Employees in DS Department

```sql
SELECT *
FROM employees
WHERE department = 'DS';
```

### Employees earning more than ₹22,00,000

```sql
SELECT name, salary
FROM employees
WHERE salary > 2200000;
```

## Key Learnings

- WHERE filters rows, not columns.
- SQL first reads the table and then applies the condition.
- Use comparison operators to create conditions.
- Always think about the business requirement before writing the query.
- Retrieve only the required columns whenever possible.
