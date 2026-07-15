# Day 18 - SELF JOIN

## What is a SELF JOIN?

A SELF JOIN is a JOIN where a table is joined with itself.

It is used when one row of a table is related to another row of the same table.

Example:

Employee → Manager

Both employees and managers are stored in the same employees table.

---

## Why Do We Need SELF JOIN?

Suppose the employees table contains:

| emp_id | emp_name | manager_id |
|--------|----------|------------|
|101|Vibhav|103|
|103|Naman|105|
|105|Priya|NULL|

The table tells us:

Vibhav's manager_id = 103

But it doesn't tell us the manager's name.

To find the manager's name, SQL has to look inside the same table again.

This is why SELF JOIN is used.

---

## Aliases

Since the same table is used twice, aliases help SQL distinguish between the two roles.

```sql
employees AS e
employees AS m
```

Here:

- e → Employee
- m → Manager

Both refer to the same table.

---

## The Bridge

The employee stores the manager's employee ID.

Therefore, the relationship is:

```sql
e.manager_id = m.emp_id
```

This is the most important line in a SELF JOIN.

---

## Basic SELF JOIN

```sql
SELECT
    e.emp_name AS Employee,
    m.emp_name AS Manager
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.emp_id;
```

---

## Why LEFT JOIN?

Some employees (like the CEO) have no manager.

Using LEFT JOIN ensures every employee appears in the result.

The manager column becomes NULL for employees without a manager.

---

## Common Mistake

Incorrect:

```sql
ON e.emp_id = m.manager_id
```

Correct:

```sql
ON e.manager_id = m.emp_id
```

Always ask:

"Who stores the manager's ID?"

Answer:

The employee.

---

## Interview Tip

Whenever one row points to another row in the same table, think:

SELF JOIN.
