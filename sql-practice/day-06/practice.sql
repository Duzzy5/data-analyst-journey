```sql
CREATE DATABASE xcompany;

USE xcompany;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    age TINYINT,
    salary INT
);

INSERT INTO employees
VALUES
(1, 'Duzzy', 'Data Science', 22, 2400000),
(2, 'NEERAJ', 'CSF', 23, 1200000),
(3, 'AAYAN', 'AIML', 17, 1800000),
(4, 'DHIREN', 'CSF', 19, 2200000),
(5, 'RUDRA', 'AIML', 20, 2000000),
(6, 'NAMAN', 'CLOUD', 22, 2100000),
(7, 'AARNAV', 'CLOUD', 20, 1900000),
(8, 'NAVANSHOE', 'AIML', 21, 18);

-- Revision Queries

SELECT *
FROM employees;

SELECT
    name,
    salary
FROM employees;

SELECT
    name,
    salary
FROM employees
WHERE age < 20;

SELECT
    id,
    name
FROM employees
ORDER BY salary DESC;

SELECT
    id,
    name,
    salary
FROM employees
WHERE age > 20
ORDER BY salary DESC
LIMIT 3;

SELECT DISTINCT department
FROM employees;

SELECT DISTINCT age
FROM employees
ORDER BY age DESC;

-- Day 06 Practice

SELECT
    name AS Employee_Name
FROM employees;

SELECT
    department AS Department_Name
FROM employees;

SELECT
    salary AS Salary,
    age AS Employee_Age
FROM employees;

SELECT
    name,
    salary,
    salary * 12 AS Annual_Salary
FROM employees;

SELECT
    name AS Employee_Name,
    department AS Department,
    salary AS Monthly_Salary
FROM employees
ORDER BY salary DESC;
```
