# Day 12 - SQL Translation & Revision

## Today's Goal

Today's focus was not learning a new SQL keyword.

Instead, the goal was to learn how to translate business questions into SQL.

## The SQL Thinking Framework

Before writing any SQL query, answer these four questions:

### Step 1

What is the business asking?

Example:

> Count students who have not provided an email.

### Step 2

Is this a Detail Query or a Summary Query?

* Detail Query → Individual records
* Summary Query → One summarized answer

### Step 3

Do I need GROUP BY?

Think of these keywords:

* each
* every
* per
* by

If they are present, GROUP BY is often required.

### Step 4

Which SQL concepts solve this problem?

Examples:

* WHERE
* GROUP BY
* HAVING
* COUNT()
* SUM()
* AVG()
* ORDER BY
* LIMIT

Only after answering these questions should you start writing SQL.

## Business Question vs SQL

Business Question:

> Show the top 3 highest-paid employees.

SQL:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

Business Question:

> How many employees work in each department?

SQL:

```sql
SELECT
    department,
    COUNT(*)
FROM employees
GROUP BY department;
```

## Interview Tip

Interviewers usually describe a business problem, not a SQL keyword.

Your first job is to identify the business requirement before thinking about syntax.
