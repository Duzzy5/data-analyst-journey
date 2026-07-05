```sql
USE sql_practice;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO students
VALUES
(1, 'Duzzy', 'duzzy@gmail.com'),
(2, 'Rudra', NULL),
(3, 'Naman', 'naman@gmail.com'),
(4, 'Aayan', NULL),
(5, 'Vibhav', 'vibhav@gmail.com');

-- Task 1
SELECT *
FROM students
WHERE email IS NULL;

-- Task 2
SELECT *
FROM students
WHERE email IS NOT NULL;

-- Task 3
SELECT
    name,
    email
FROM students
WHERE email IS NOT NULL;

-- Task 4
SELECT COUNT(*) AS not_given_email
FROM students
WHERE email IS NULL;

-- Task 5
SELECT COUNT(*) AS given_email
FROM students
WHERE email IS NOT NULL;
```
