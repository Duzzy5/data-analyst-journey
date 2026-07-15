# Day 18 Learnings

## Biggest Learning

A SELF JOIN is not a new type of relationship.

It is simply one table playing two different roles.

Example:

Employee → Manager

Both are stored in the same table.

---

## What I Learned

- SELF JOIN joins a table with itself.
- Aliases are necessary because SQL must treat the same table as two different roles.
- The bridge in this dataset is:

e.manager_id = m.emp_id

- LEFT JOIN is preferred because some employees may not have managers.

---

## Mistakes I Made

### Mistake 1

I reversed the bridge.

Incorrect:

e.emp_id = m.manager_id

Correct:

e.manager_id = m.emp_id

---

### Mistake 2

I used INNER JOIN while searching for employees without managers.

Since employees without managers don't have matching rows, LEFT JOIN is the correct choice.

---

## Confidence Check

✅ I understand why SELF JOIN exists.

✅ I know why aliases are necessary.

✅ I understand that one table can represent two different roles.

⚠️ I need more practice identifying the correct bridge.

---

## Interview Takeaway

When solving SELF JOIN questions, first ask:

1. What are the two roles?

Example:

Employee

Manager

2. Which column connects them?

Once the bridge is identified, the SQL becomes much easier.

---

## Mentor's Advice

Do not memorize SELF JOIN syntax.

Instead, identify:

- The two roles.
- The bridge connecting them.

The syntax will naturally follow.
