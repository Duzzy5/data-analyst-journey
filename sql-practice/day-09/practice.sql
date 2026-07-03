```sql
USE sql_practice;

-- Count employees in each department
SELECT
    department,
    COUNT(*)
FROM employees
GROUP BY department;

-- Average salary in each department
SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department;

-- Highest salary in each department
SELECT
    department,
    MAX(salary)
FROM employees
GROUP BY department;

-- Count employees in each city
SELECT
    city,
    COUNT(*)
FROM employees
GROUP BY city;

-- Total salary paid in each department
SELECT
    department,
    SUM(salary)
FROM employees
GROUP BY department;

-- Bonus Practice
SELECT
    city,
    AVG(salary)
FROM employees
GROUP BY city;
```
