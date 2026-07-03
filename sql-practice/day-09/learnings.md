# Day 09 Learnings

## What I Learned

* `GROUP BY` groups rows with the same values.
* Aggregate functions are calculated separately for each group.
* Keywords like **each**, **every**, **per**, and **by** usually indicate that `GROUP BY` is needed.
* `COUNT(*)` is generally preferred over `COUNT(column_name)` when counting rows.

## Confidence Check

✅ I can count employees in each department.

✅ I can calculate average, maximum, and total salary for each department.

✅ I understand that SQL groups the data first and then applies aggregate functions.

## Interview Takeaway

`GROUP BY` is one of the most important SQL clauses for Data Analysts because it helps summarize data by categories such as departments, cities, products, or customer segments.
