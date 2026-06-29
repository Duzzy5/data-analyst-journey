```sql
CREATE DATABASE x_company;

USE x_company;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    age TINYINT,
    salary INT
);

INSERT INTO employees
VALUES
(1, 'DUZZY', 'DS', 22, 2400000),
(2, 'AAYAN', 'AI ML', 21, 1000000),
(3, 'NAMAN', 'CLOUD', 22, 1400000),
(4, 'RUDRA', 'AI ML', 21, 1400000),
(5, 'ABHINAV', 'CSF', 21, 1000000),
(6, 'NEERAJ', 'FRONTEND', 22, 1800000);

-- Display all records
SELECT *
FROM employees;

-- Display selected columns
SELECT
    id,
    name,
    age
FROM employees;

-- Employees with salary greater than 12,00,000
SELECT
    department,
    salary
FROM employees
WHERE salary > 1200000;

-- Sort salary in ascending order
SELECT *
FROM employees
ORDER BY salary ASC;

-- Sort salary in descending order
SELECT *
FROM employees
ORDER BY salary DESC;

-- Display name and salary sorted by highest salary
SELECT
    name,
    salary
FROM employees
ORDER BY salary DESC;

-- Sort employees alphabetically by name
SELECT *
FROM employees
ORDER BY name ASC;

-- Sort employees by department
SELECT *
FROM employees
ORDER BY department ASC;
```
