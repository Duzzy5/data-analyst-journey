# Day 14 Learnings

## Biggest Learning

Today I solved business requirements instead of topic-based SQL questions.

This helped me think more like a Data Analyst.

---

## What Improved

* I selected SQL concepts based on business requirements.
* I became more comfortable combining multiple SQL concepts in a single query.
* I used GROUP BY and HAVING without needing hints.
* I naturally identified when aggregate functions were required.

---

## Mistakes to Remember

### 1. Read business requirements carefully.

I sometimes confuse:

* more than 2 (`> 2`)
* at least 2 (`>= 2`)

This is a requirement-reading mistake, not a SQL syntax mistake.

---

### 2. Detail Query vs Summary Query

* Detail Query returns individual records.
* Summary Query returns summarized information.

I should identify this before writing SQL.

---

### 3. ORDER BY Direction

If the business asks for:

* Highest
* Largest
* Maximum
* Top

I should think:

```sql
DESC
```

If the business asks for:

* Lowest
* Smallest
* Minimum

I should think:

```sql
ASC
```

---

## Confidence Check

✅ I can solve business-style SQL questions.

✅ I understand how multiple SQL clauses work together.

✅ I know when to use WHERE and HAVING.

✅ I can identify when GROUP BY is required.

---

## Interview Takeaway

SQL interviews rarely ask:

> "Write a GROUP BY query."

Instead, they present a business problem.

My job is to identify the business requirement first and then choose the appropriate SQL concepts to solve it.

This is the mindset I want to continue developing.
