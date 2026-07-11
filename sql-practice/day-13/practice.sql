```sql
USE sql_practice;

-- Task 1
-- HR wants to know how many employees work in the company.

SELECT COUNT(*)
FROM employees;

-- Task 2
-- Finance wants the three highest-paid employees.

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- Task 3
-- CEO wants the average salary in each department.

SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department;

-- Task 4
-- HR wants cities having at least two employees.

SELECT
    city,
    COUNT(*)
FROM employees
GROUP BY city
HAVING COUNT(*) >= 2;

-- Task 5
-- CTO wants departments whose average salary is greater than ₹20,00,000.

SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 2000000;
```
