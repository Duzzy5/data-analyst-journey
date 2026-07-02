```sql
CREATE DATABASE IF NOT EXISTS sql_practice;

USE sql_practice;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    city VARCHAR(50),
    age TINYINT,
    salary INT
);

INSERT INTO employees
VALUES
(1, 'Duzzy', 'Data Science', 'Dehradun', 22, 2400000),
(2, 'Neeraj', 'CSF', 'Delhi', 23, 1200000),
(3, 'Aayan', 'AIML', 'Mumbai', 17, 1800000),
(4, 'Dhiren', 'CSF', 'Delhi', 19, 2200000),
(5, 'Rudra', 'AIML', 'Pune', 20, 2000000),
(6, 'Naman', 'Cloud', 'Bengaluru', 22, 2100000),
(7, 'Aarnav', 'Cloud', 'Mumbai', 20, 1900000),
(8, 'Navanshoe', 'AIML', 'Delhi', 21, 1800000),
(9, 'Vibhav', 'Data Science', 'Dehradun', 21, 2500000),
(10, 'Ankit', 'Cloud', 'Pune', 24, 1700000);

-- Count total employees
SELECT COUNT(*)
FROM employees;

-- Total salary
SELECT SUM(salary)
FROM employees;

-- Average salary
SELECT AVG(salary)
FROM employees;

-- Highest salary
SELECT MAX(salary)
FROM employees;

-- Lowest salary
SELECT MIN(salary)
FROM employees;
```
