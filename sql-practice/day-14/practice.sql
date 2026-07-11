```sql
USE company_db;

-- Total Employees
SELECT COUNT(*)
FROM employees;

-- Top 5 Highest Paid Employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;

-- Average Salary by Department
SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department;

-- Cities Having At Least 2 Employees
SELECT
    city,
    COUNT(*)
FROM employees
GROUP BY city
HAVING COUNT(*) >= 2;

-- Departments with Average Salary Greater Than ₹20,00,000
SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 2000000;

-- Youngest Employee
SELECT *
FROM employees
ORDER BY age ASC
LIMIT 1;

-- Department with Highest Salary Expenditure
SELECT
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC
LIMIT 1;

-- Students Without Email
SELECT *
FROM students
WHERE email IS NULL;

-- Count Students With Email
SELECT COUNT(*) AS students_with_email
FROM students
WHERE email IS NOT NULL;

-- Department Report
SELECT
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY average_salary DESC;
```
