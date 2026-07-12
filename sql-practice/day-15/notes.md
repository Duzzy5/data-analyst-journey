# Day 15 - INNER JOIN (Part 1)

## Why Do We Need JOINS?

In real databases, related information is stored in different tables instead of one large table.

Example:

### employees

| emp_id | emp_name | department_id | salary  |
| ------ | -------- | ------------- | ------- |
| 101    | Vibhav   | 1             | 2400000 |
| 102    | Rudra    | 2             | 1900000 |

### departments

| department_id | department_name |
| ------------- | --------------- |
| 1             | Data Science    |
| 2             | Cloud           |
| 3             | HR              |
| 4             | Finance         |

The `employees` table knows only the `department_id`.

The `departments` table knows the `department_name`.

To display both employee names and department names together, SQL uses a JOIN.

---

# What is INNER JOIN?

An `INNER JOIN` combines rows from two tables where the values in the common column match.

Think of it as connecting two puzzle pieces using a common key.

---

# Syntax

```sql
SELECT column1, column2
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;
```

---

# Understanding the ON Clause

`ON` tells SQL how the two tables are related.

Example:

```sql
ON employees.department_id = departments.department_id
```

SQL matches rows where the department IDs are equal.

---

# Why Store department_id Instead of department_name?

Instead of storing:

Data Science

thousands of times,

we store:

```text
department_id = 1
```

Benefits:

* Less duplicate data (less redundancy)
* Less storage
* Easier updates
* Better database design

---

# Data Redundancy

Data redundancy means storing the same information repeatedly.

Example:

```
Vibhav     Data Science
Naman      Data Science
Rahul      Data Science
```

Instead of repeating "Data Science", databases store a single department record and reference it using an ID.

---

# Common INNER JOIN Examples

Employee name with department name

```sql
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

Employee name, department and salary

```sql
SELECT
    employees.emp_name,
    departments.department_name,
    employees.salary
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

Employees working in Cloud department

```sql
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_name = 'Cloud';
```

Employees earning more than ₹20,00,000

```sql
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE employees.salary > 2000000;
```

Order employees by department name

```sql
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
ORDER BY departments.department_name;
```

---

# Interview Tip

Always ask yourself:

* Which table contains the data I need?
* What is the common column connecting these tables?

That common column becomes the JOIN condition.
