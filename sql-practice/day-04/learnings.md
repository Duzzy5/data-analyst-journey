# Day 04 Learnings

## What I Learned

* `LIMIT` is used to restrict the number of rows returned by a query.
* `LIMIT` is most useful when combined with `ORDER BY`.
* `ORDER BY salary DESC LIMIT 1` returns the highest-paid employee.
* `LIMIT` can be used independently, but combining it with `ORDER BY` gives meaningful results.

## Confidence Check

✅ I can retrieve the first N rows using `LIMIT`.

✅ I can find the highest-paid or youngest employee using `ORDER BY` and `LIMIT`.

✅ I understand that `ORDER BY` executes before `LIMIT`.

## Interview Takeaway

To retrieve the Top N records:

1. Sort the data using `ORDER BY`.
2. Restrict the result using `LIMIT`.
