# Day 16 Learnings

## Biggest Learning

INNER JOIN and LEFT JOIN are almost identical in syntax.

The only difference is the rows they return.

---

## What I Learned

* INNER JOIN returns only matching rows.
* LEFT JOIN returns every row from the left table.
* If no match exists, the right table columns become NULL.
* The ON clause defines how two tables are related.
* The common column is usually a Primary Key / Foreign Key relationship.

---

## Mistakes to Remember

Today I learned an important professional habit.

Instead of writing:

```sql
WHERE department_id IS NULL;
```

I should specify the table:

```sql
WHERE departments.department_id IS NULL;
```

This avoids ambiguity and makes the query easier to read.

---

## Confidence Check

✅ I understand why LEFT JOIN exists.

✅ I can explain the difference between INNER JOIN and LEFT JOIN.

✅ I can identify unmatched rows using LEFT JOIN.

✅ I understand why professional SQL qualifies column names with their table names.

---

## Interview Takeaway

Always ask:

1. Which table is guaranteed to appear?
2. Which table may have missing matches?

The answer helps determine whether INNER JOIN or LEFT JOIN is appropriate.
