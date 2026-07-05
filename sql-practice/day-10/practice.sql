```sql
USE sql_practice;

-- Task 1: Departments having more than 2 employees
SELECT
    department,
    COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- Task 2: Cities where the average salary is greater than ₹18,00,000
SELECT
    city,
    AVG(salary)
FROM employees
GROUP BY city
HAVING AVG(salary) > 1800000;

-- Task 3: Departments whose total salary is greater than ₹50,00,000
SELECT
    department,
    SUM(salary)
FROM employees
GROUP BY department
HAVING SUM(salary) > 5000000;

-- Task 4: Cities having at least 2 employees
SELECT
    city,
    COUNT(*)
FROM employees
GROUP BY city
HAVING COUNT(*) >= 2;

-- Task 5: Departments where the highest salary is greater than ₹22,00,000
SELECT
    department,
    MAX(salary)
FROM employees
GROUP BY department
HAVING MAX(salary) > 2200000;
```
