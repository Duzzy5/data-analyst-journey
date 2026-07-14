# Day 17 Learnings

## Biggest Learning

RIGHT JOIN is not a completely new concept.

It is simply another way of deciding which table should always appear in the result.

---

## What I Learned

* INNER JOIN returns only matching rows.
* LEFT JOIN preserves every row from the left table.
* RIGHT JOIN preserves every row from the right table.
* Missing matches produce `NULL` values in the columns of the other table.
* To find unmatched rows, check for `NULL` values in the table that failed to match.

---

## Professional Insight

A RIGHT JOIN can often be rewritten as a LEFT JOIN by swapping the table order.

Example:

```sql
employees LEFT JOIN departments
```

is equivalent to:

```sql
departments RIGHT JOIN employees
```

Choosing between them is usually about readability and which table you want to treat as the primary table.

---

## Mistakes to Remember

* LEFT JOIN and RIGHT JOIN are **not** based on where existing `NULL` values are stored.
* They are based on **which table is preserved** in the final result.
* Always qualify column names with their table names when multiple tables contain similar columns.

---

## Confidence Check

✅ I understand the difference between INNER, LEFT, and RIGHT JOIN.

✅ I can identify unmatched rows using `NULL` after a JOIN.

✅ I know that table order changes the behavior of LEFT and RIGHT JOIN.

✅ I understand that many RIGHT JOIN queries can be rewritten as LEFT JOIN queries by swapping the table order.

---

## Interview Takeaway

When choosing a JOIN, first decide:

> Which table must always appear in the result?

Once that is clear, selecting the correct JOIN becomes much easier.
