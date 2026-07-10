# Day 12 Learnings

## Biggest Learning

My biggest challenge is no longer SQL syntax.

My challenge is translating business requirements into SQL.

Going forward, I will always think before I type.

## Common Mistakes I Made

1. Reading the business question too quickly.
2. Confusing `DISTINCT` and `GROUP BY`.
3. Sometimes writing `TOTAL()` instead of `SUM()`.
4. Explaining what a query does instead of its logical execution order.
5. Forgetting that `GROUP BY` is only needed when the business asks for results **per group**.

## My New Problem-Solving Process

For every SQL question:

1. What is the business asking?
2. Detail query or summary query?
3. Do I need GROUP BY?
4. Which SQL concepts are required?
5. Write the SQL.

## Revision Questions

1. Difference between `WHERE` and `HAVING`.
2. When should `DISTINCT` be preferred over `GROUP BY`?
3. Explain the logical execution order of a SQL query.
4. When do you use `COUNT(*)` instead of `COUNT(column_name)`?
5. What is the difference between `NULL` and an empty string?
6. Give one business question that requires `GROUP BY`.
7. Give one business question that requires `HAVING`.
8. Explain why `WHERE AVG(salary)` is invalid.
9. Write a query to find the average salary in each department.
10. Write a query to count students who have not provided an email.

## Confidence Check

✅ I understand the SQL concepts learned so far.

✅ I know my weak areas.

✅ My focus is now on translating business language into SQL instead of memorizing syntax.
