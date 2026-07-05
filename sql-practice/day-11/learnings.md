# Day 11 Learnings

## What I Learned

* `NULL` represents missing or unknown data.
* `NULL` is different from an empty string (`''`) and from the value `0`.
* To check for missing values, use `IS NULL`.
* To check for existing values, use `IS NOT NULL`.
* `COUNT()` can be combined with `WHERE` to count filtered rows.
* `GROUP BY` is only needed when the business question asks for grouped results.

## Biggest Lesson Today

I realized that my main challenge is not SQL syntax.

My challenge is translating business questions into SQL.

Going forward, I will first identify:

1. What is the business asking?
2. Is it a detail query or a summary query?
3. Do I need `GROUP BY`?
4. Which SQL concepts solve this problem?

Only then will I write the SQL query.

## Confidence Check

✅ I can identify NULL values.

✅ I can filter rows using `IS NULL` and `IS NOT NULL`.

✅ I know when `GROUP BY` is unnecessary.

## Interview Takeaway

The most common beginner mistake is writing:

```sql
WHERE email = NULL;
```

The correct syntax is:

```sql
WHERE email IS NULL;
```

Always remember that `NULL` is not a value—it represents unknown or missing information.
