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

-- Display first 3 employees
SELECT *
FROM employees
LIMIT 3;

-- Display the highest-paid employee
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;

-- Display the top 2 highest-paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 2;

-- Display the youngest employee
SELECT *
FROM employees
ORDER BY age ASC
LIMIT 1;

-- Display name and department of the first 4 employees
SELECT
    name,
    department
FROM employees
LIMIT 4;
```
