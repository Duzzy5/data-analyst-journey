# Day 19 - Thinking in Relationships

## Goal

Today's objective was not to learn a new SQL keyword.

The goal was to understand HOW tables are related and WHY JOINs work.

---

# What is a Relationship?

A relationship is a connection between two pieces of data.

Example:

Employee → Department

Employee → Manager

Order → Customer

Student → Course

Relationships allow us to connect related information.

---

# Why Do We Need Relationships?

Instead of storing duplicate information thousands of times, databases store it once and connect tables using IDs.

Example:

Employees

| emp_id | emp_name | department_id |
|--------|----------|---------------|
|101|Vibhav|1|

Departments

| department_id | department_name |
|---------------|-----------------|
|1|Data Science|

department_id is the connection between both tables.

---

# What is a Bridge?

A bridge is the common relationship between two tables (or two roles of the same table).

Example:

employees.department_id
        =
departments.department_id

This bridge tells SQL how both tables are connected.

---

# SELF JOIN Bridge

Employee table

| emp_id | emp_name | manager_id |
|--------|----------|------------|
|101|Vibhav|103|

manager_id points to another employee.

That employee has

emp_id = 103

Therefore,

Bridge:

e.manager_id = m.emp_id

Employee points to Manager.

---

# Can We Reverse It?

These are mathematically identical:

e.manager_id = m.emp_id

m.emp_id = e.manager_id

SQL treats both the same.

However,

e.manager_id = m.emp_id

is preferred because it clearly explains the relationship.

Read it as:

Employee's manager_id points to Manager's emp_id.

---

# JOIN Types

INNER JOIN

Returns only matching rows.

LEFT JOIN

Returns every row from the left table, even if no match exists.

RIGHT JOIN

Returns every row from the right table, even if no match exists.

SELF JOIN

Not a new JOIN type.

It simply means joining a table with itself.

A SELF JOIN can use:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN

depending on the business requirement.

---

# Business Thinking

Before writing SQL ask:

1. What is the business asking?
2. Which tables (or roles) are involved?
3. What is the bridge?
4. Which JOIN should I use?
5. Do I need GROUP BY, ORDER BY or Aggregate Functions?

Only then write SQL.
