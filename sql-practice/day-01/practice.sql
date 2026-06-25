CREATE DATABASE practice;

USE practice;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary FLOAT,
    age TINYINT
);

INSERT INTO employees (
    id,
    name,
    department,
    salary,
    age
)
VALUES
(1, 'Duzzy', 'DS', 2400000, 22),
(2, 'Vibhav', 'DS', 2300000, 21),
(3, 'Rudra', 'DS', 24500000, 20),
(4, 'Naman', 'DS', 500000, 22),
(5, 'Abhinav', 'DS', 2100000, 21),
(6, 'Navrose', 'DS', 2300000, 22);

-- Task 1
SELECT *
FROM employees;

-- Task 2
SELECT
    name,
    salary
FROM employees;

-- Task 3
SELECT department
FROM employees;

-- Task 4
SELECT
    age,
    name
FROM employees;
