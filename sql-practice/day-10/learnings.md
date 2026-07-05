# Day 10 Learnings

## What I Learned

* `HAVING` filters grouped data after `GROUP BY`.
* `WHERE` filters rows before grouping.
* Aggregate functions like `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()` are commonly used with `HAVING`.
* SQL first groups the data and then applies the `HAVING` condition.

## Confidence Check

✅ I can distinguish between `WHERE` and `HAVING`.

✅ I can filter groups using aggregate functions.

✅ I can answer business questions such as:

* Which departments have more than 2 employees?
* Which cities have an average salary above a certain value?
* Which departments have the highest total salary?

## Interview Takeaway

Remember this sequence:

**FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT**

A simple memory trick:

* **WHERE** filters **people** (rows).
* **HAVING** filters **teams** (groups).
