# Day 17 - RIGHT JOIN

## What is RIGHT JOIN?

A RIGHT JOIN returns:

* Every row from the **right table**.
* Matching rows from the **left table**.
* If no matching row exists in the left table, the left table columns become `NULL`.

---

## INNER JOIN vs LEFT JOIN vs RIGHT JOIN

### INNER JOIN

Returns only the rows that have matching values in both tables.

---

### LEFT JOIN

Returns every row from the left table.

If no match exists in the right table, the right table columns become `NULL`.

---

### RIGHT JOIN

Returns every row from the right table.

If no match exists in the left table, the left table columns become `NULL`.

---

## Syntax

```sql
SELECT columns
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id;
```

---

## Visual Understanding

### LEFT JOIN

```
Keep everything from the LEFT table.
```

### RIGHT JOIN

```
Keep everything from the RIGHT table.
```

---

## Finding Departments Without Employees

```sql
SELECT
    departments.department_name,
    employees.emp_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id
WHERE employees.department_id IS NULL;
```

When a department has no employees, every column from the `employees` table becomes `NULL`.

---

## Professional Tip

Many SQL developers prefer writing a `LEFT JOIN` instead of a `RIGHT JOIN`.

Example:

```sql
employees LEFT JOIN departments
```

is logically equivalent to:

```sql
departments RIGHT JOIN employees
```

The result depends on **which table you want to preserve**, not on which keyword looks easier.

---

## Interview Tip

Before choosing a JOIN, ask yourself:

> Which table must always appear in the final result?

That answer usually tells you which JOIN to use.
