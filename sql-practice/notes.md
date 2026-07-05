# Day 11 - NULL Handling

## What is NULL?

`NULL` represents a missing or unknown value.

It does **not** mean:

* 0
* Empty String (`''`)
* False

It simply means that the value is unknown or not available.

## Checking for NULL Values

### Find rows with missing values

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

### Find rows where values are present

```sql
SELECT *
FROM students
WHERE email IS NOT NULL;
```

## Counting NULL Values

### Count students who have not provided an email

```sql
SELECT COUNT(*) AS not_given_email
FROM students
WHERE email IS NULL;
```

### Count students who have provided an email

```sql
SELECT COUNT(*) AS given_email
FROM students
WHERE email IS NOT NULL;
```

## Important Rules

❌ Incorrect

```sql
WHERE email = NULL;
```

❌ Incorrect

```sql
WHERE email != NULL;
```

✅ Correct

```sql
WHERE email IS NULL;
```

✅ Correct

```sql
WHERE email IS NOT NULL;
```

## Key Points

* `NULL` means missing or unknown data.
* Always use `IS NULL` or `IS NOT NULL`.
* If the business asks for a single total count, use `COUNT()` with `WHERE`.
* `GROUP BY` is only required when the question asks for data **per group** (such as each department or each city).

## Interview Tip

Before writing SQL, ask yourself:

* Do I need one answer?
* Or one answer for each group?

If it's one answer, `GROUP BY` is usually unnecessary.
