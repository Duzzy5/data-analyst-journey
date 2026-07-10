```sql
USE sql_practice;

-- Show all employees
SELECT *
FROM employees;

-- Show employee name and salary
SELECT
    name,
    salary
FROM employees;

-- Employees older than 21
SELECT *
FROM employees
WHERE age > 21;

-- Highest-paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- Unique departments
SELECT DISTINCT department
FROM employees;

-- Total employees
SELECT COUNT(*)
FROM employees;

-- Average salary
SELECT AVG(salary)
FROM employees;

-- Employees in each department
SELECT
    department,
    COUNT(*)
FROM employees
GROUP BY department;

-- Departments having more than 2 employees
SELECT
    department,
    COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- Students without email
SELECT *
FROM students
WHERE email IS NULL;

-- Count students with email
SELECT COUNT(*) AS given_email
FROM students
WHERE email IS NOT NULL;
```
