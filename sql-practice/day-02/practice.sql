CREATE DATABASE practice;

USE practice;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age TINYINT
);

INSERT INTO employees
VALUES
(1, 'Duzzy', 'DS', 2400000, 22),
(2, 'Rudra', 'AI', 1400000, 22),
(3, 'Abhinav', 'AI', 900000, 22),
(4, 'Aayan', 'Cyber', 100000, 22),
(5, 'Naman', 'Cloud', 1400000, 22),
(6, 'Navrose', 'Agri', 2400000, 22);

-- Task 1
SELECT *
FROM employees
WHERE age > 21;

-- Task 2
SELECT
    name,
    salary
FROM employees
WHERE salary > 2200000;

-- Task 3
SELECT *
FROM employees
WHERE department = 'DS';

-- Task 4
SELECT *
FROM employees
WHERE age <= 21;

-- Task 5
SELECT *
FROM employees
WHERE department != 'DS';
