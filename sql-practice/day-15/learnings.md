# Day 15 Learnings

## Biggest Learning

Today's biggest lesson was understanding why relational databases use multiple tables and how INNER JOIN connects them.

I learned that JOINs are not difficult when I understand the relationship between tables.

---

## What I Learned

* Databases split information into multiple related tables.
* Related tables are connected using a common column.
* INNER JOIN returns rows where matching values exist in both tables.
* The `ON` clause defines the relationship between two tables.
* Data redundancy means storing the same information repeatedly.
* Using IDs instead of repeating text saves storage and makes updates easier.

---

## Interview Takeaways

Before writing a JOIN, ask:

1. Which table has the information I need?
2. Which table has the remaining information?
3. What is the common column between them?

If I can answer these three questions, writing the JOIN becomes straightforward.

---

## Confidence Check

✅ I understand why JOINs exist.

✅ I can identify the common column between two tables.

✅ I can write basic INNER JOIN queries.

✅ I can filter and sort data after performing an INNER JOIN.

---

## Mistakes to Remember

* Always qualify column names when multiple tables contain similar column names.
* Think about the relationship first, then write the SQL.
* JOIN connects related tables; it does not create new data.
