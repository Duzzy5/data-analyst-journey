```sql
CREATE DATABASE IF NOT EXISTS company_db;

USE company_db;

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department_id INT,
    salary INT
);

INSERT INTO employees VALUES
(101,'Vibhav',1,2400000),
(102,'Rudra',2,1900000),
(103,'Naman',1,2100000),
(104,'Aayan',3,1500000),
(105,'Neeraj',2,2200000),
(106,'Priya',4,1700000);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(1,'Data Science'),
(2,'Cloud'),
(3,'HR'),
(4,'Finance');

-- Employee Name and Department Name
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;

-- Employee Name, Department and Salary
SELECT
    employees.emp_name,
    departments.department_name,
    employees.salary
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;

-- Employees Working in Cloud Department
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_name = 'Cloud';

-- Employees Earning More Than ₹20,00,000
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE employees.salary > 2000000;

-- Employees Ordered by Department Name
SELECT
    employees.*,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
ORDER BY departments.department_name;
```
