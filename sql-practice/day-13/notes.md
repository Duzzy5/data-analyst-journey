notes.md# Day 13 - Business Thinking with SQL

## Today's Goal

Today's focus was to solve business problems instead of writing SQL based on topic names.

The objective was to translate business requirements into SQL.

## SQL Thinking Framework

Before writing any query, answer these questions:

### Step 1

What is the business asking?

### Step 2

Is it a Detail Query or a Summary Query?

* Detail Query → Returns individual records.
* Summary Query → Returns summarized information.

### Step 3

Do I need GROUP BY?

Think of keywords like:

* each
* every
* per
* by

If these appear, GROUP BY is usually required.

### Step 4

Which SQL concepts are required?

Examples:

* SELECT
* WHERE
* ORDER BY
* LIMIT
* GROUP BY
* HAVING
* Aggregate Functions

### Step 5

Write the SQL query.

## Detail vs Summary

### Detail Query

Returns individual rows.

Example:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

### Summary Query

Returns summarized information.

Example:

```sql
SELECT AVG(salary)
FROM employees;
```

## Key Learning

Do not think:

> Which SQL keyword should I use?

Instead think:

> What is the business asking me to find?

The SQL syntax becomes much easier after understanding the business requirement.

## Interview Tip

Interviewers rarely ask:

> "Write a GROUP BY query."

Instead, they ask:

> "Find the average salary in each department."

Your first task is to recognize the business requirement.
