USE sql_company;

-- View Tables
SELECT * FROM employees;

SELECT * FROM departments;

---------------------------------------------------------
-- Question 1
-- Show every employee with their manager
---------------------------------------------------------

SELECT
    e.emp_name AS Employee,
    m.emp_name AS Manager
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.emp_id;

---------------------------------------------------------
-- Question 2
-- Show every employee, salary and manager
---------------------------------------------------------

SELECT
    e.emp_name,
    e.salary,
    m.emp_name AS Manager
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.emp_id;

---------------------------------------------------------
-- Question 3
-- Show employees who do not report to anyone
---------------------------------------------------------

SELECT
    e.emp_name,
    e.salary,
    e.city
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.emp_id
WHERE e.manager_id IS NULL;

---------------------------------------------------------
-- Question 4
-- Count employees under every manager
---------------------------------------------------------

SELECT
    m.emp_id,
    m.emp_name AS Manager,
    COUNT(e.emp_id) AS Total_Employees
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.emp_id
GROUP BY
    m.emp_id,
    m.emp_name
ORDER BY Total_Employees DESC;

---------------------------------------------------------
-- Question 5
-- Employees earning more than their managers
---------------------------------------------------------

SELECT
    e.emp_name AS Employee,
    e.salary AS Employee_Salary,
    m.emp_name AS Manager,
    m.salary AS Manager_Salary
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;

---------------------------------------------------------
-- Question 6
-- Show employees ordered by manager name
---------------------------------------------------------

SELECT
    e.emp_name,
    m.emp_name AS Manager
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.emp_id
ORDER BY m.emp_name;

---------------------------------------------------------
-- Question 7
-- Average salary under every manager
---------------------------------------------------------

SELECT
    m.emp_name AS Manager,
    AVG(e.salary) AS Average_Salary
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.emp_id
GROUP BY
    m.emp_id,
    m.emp_name;

---------------------------------------------------------
-- Question 8
-- Employees working in Data Science department
---------------------------------------------------------

SELECT
    e.emp_name,
    d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id
WHERE d.department_name = 'Data Science';

---------------------------------------------------------
-- Question 9
-- Average salary of each department
---------------------------------------------------------

SELECT
    d.department_name,
    AVG(e.salary) AS Average_Salary
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id
GROUP BY
    d.department_id,
    d.department_name;

---------------------------------------------------------
-- Question 10
-- Department with the highest average salary
---------------------------------------------------------

SELECT
    d.department_name,
    AVG(e.salary) AS Average_Salary
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id
GROUP BY
    d.department_id,
    d.department_name
ORDER BY Average_Salary DESC
LIMIT 1;
