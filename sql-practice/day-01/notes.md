# Day 01 - Database Basics & SELECT

## What is a Database?

A database is an organized collection of data that allows us to Create, Read, Update, and Delete (CRUD) information efficiently. It contains multiple related tables.

## What is a Table?

A table is an object inside a database that stores related data in rows and columns.

Example:

| ID | Name | Department | Salary |
|----|------|------------|--------|
| 1  | Duzzy | DS | 2400000 |

## What is SQL?

SQL (Structured Query Language) is used to communicate with databases. It helps us retrieve, insert, update, and delete data.

## SELECT Statement

The `SELECT` statement is used to retrieve data from a table.

### Select all columns

```sql
SELECT * FROM employees;
```

### Select specific columns

```sql
SELECT name, salary
FROM employees;
```

## Key Learnings

- A database contains multiple tables.
- A table stores data in rows and columns.
- `SELECT *` returns every column.
- Select only the columns you actually need.
- Think about the business question before writing SQL.
