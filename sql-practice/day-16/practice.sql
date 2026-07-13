```sql
USE company_db;

-- LEFT JOIN
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;

-- INNER JOIN
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;

-- Employee Name, Salary and Department
SELECT
    employees.emp_name,
    employees.salary,
    departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;

-- Employees without a matching department
SELECT
    employees.emp_name,
    departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_id IS NULL;
```
