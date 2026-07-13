# Day 16 - LEFT JOIN

## What is LEFT JOIN?

A LEFT JOIN returns:

* Every row from the left table.
* Matching rows from the right table.
* If no match exists, the columns from the right table become NULL.

---

## Difference Between INNER JOIN and LEFT JOIN

### INNER JOIN

Returns only matching rows.

Example:

Employee without a department will NOT appear.

---

### LEFT JOIN

Returns all rows from the left table.

If an employee has no department, the employee still appears and the department columns become NULL.

---

## Syntax

```sql
SELECT columns
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

---

## Why LEFT JOIN?

LEFT JOIN is useful when the business wants:

* All employees
* All customers
* All orders

Even if related information is missing.

---

## Important Concept

The left table is always fully preserved.

The right table contributes data only when a matching row exists.

---

## Finding Missing Matches

Employees without departments:

```sql
SELECT employees.emp_name,
       departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_id IS NULL;
```

---

## Interview Tip

Think of LEFT JOIN as:

"Show everyone from the left table, even if there is no match."
