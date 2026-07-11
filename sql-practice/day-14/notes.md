# Day 14 - Business Case Study (SQL in Real-World Scenarios)

## Today's Goal

Today's objective was to solve business problems using SQL instead of practicing isolated SQL concepts.

The focus was on selecting the correct SQL concepts based on the business requirement.

---

# Business Thinking Process

Before writing SQL, think in this order:

### Step 1

Understand the business requirement.

### Step 2

Decide whether the query is:

* Detail Query
* Summary Query

### Step 3

Determine whether GROUP BY is required.

Look for words such as:

* each
* every
* per
* by

### Step 4

Choose the required SQL concepts.

Possible concepts include:

* SELECT
* WHERE
* ORDER BY
* LIMIT
* COUNT()
* SUM()
* AVG()
* MAX()
* MIN()
* GROUP BY
* HAVING

### Step 5

Write the SQL query.

---

# Business Scenarios Practiced

### Count total employees

```sql
SELECT COUNT(*)
FROM employees;
```

---

### Top 5 highest-paid employees

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

---

### Average salary in each department

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

---

### Cities having at least two employees

```sql
SELECT city, COUNT(*)
FROM employees
GROUP BY city
HAVING COUNT(*) >= 2;
```

---

### Departments whose average salary is greater than ₹20,00,000

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 2000000;
```

---

### Youngest employee

```sql
SELECT *
FROM employees
ORDER BY age ASC
LIMIT 1;
```

---

### Department with the highest salary expenditure

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department
ORDER BY SUM(salary) DESC
LIMIT 1;
```

---

### Students without an email

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

---

### Count students with an email

```sql
SELECT COUNT(*)
FROM students
WHERE email IS NOT NULL;
```

---

### Department Report

```sql
SELECT
    department,
    COUNT(*),
    AVG(salary)
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY AVG(salary) DESC;
```

---

# Interview Tip

Business questions rarely mention SQL keywords.

Your job is to convert business language into SQL logic.
