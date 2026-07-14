```sql
USE company_db;

-- Employee Name and Department Name
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id;

-- Department Name and Employee Salary
SELECT
    departments.department_name,
    employees.salary
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id;

-- Departments With No Employees
SELECT
    departments.department_name,
    employees.emp_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id
WHERE employees.department_id IS NULL;

-- Departments Ordered Alphabetically
SELECT
    departments.department_name,
    employees.emp_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id
ORDER BY departments.department_name ASC;

-- Equivalent LEFT JOIN
SELECT
    departments.department_name,
    employees.emp_name
FROM departments
LEFT JOIN employees
ON departments.department_id = employees.department_id;
```
