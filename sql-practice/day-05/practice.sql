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

-- Display unique departments
SELECT DISTINCT department
FROM employees;

-- Display unique ages
SELECT DISTINCT age
FROM employees;

-- Display unique salary values
SELECT DISTINCT salary
FROM employees;

-- Display unique combinations of department and age
SELECT DISTINCT
    department,
    age
FROM employees;

-- Display unique departments in alphabetical order
SELECT DISTINCT department
FROM employees
ORDER BY department ASC;
```
