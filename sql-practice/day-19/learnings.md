# Day 19 Learnings

## Biggest Realization

JOINs are not about SQL syntax.

JOINs are about relationships between data.

Once the relationship is identified, writing SQL becomes much easier.

---

# Things I Learned

✔ Relationships connect related data.

✔ A bridge is the common column that connects two tables (or two roles of the same table).

✔ SELF JOIN is simply joining one table with itself.

✔ SELF JOIN can use INNER JOIN, LEFT JOIN or RIGHT JOIN depending on the requirement.

✔ Equality in the ON clause is symmetric.

These produce the same result:

e.manager_id = m.emp_id

m.emp_id = e.manager_id

The preferred version is chosen for readability.

---

# Mistakes I Made

## Mistake 1

I initially thought SELF JOIN always uses INNER JOIN.

Correction:

SELF JOIN only describes the tables.

INNER, LEFT and RIGHT describe how matching should happen.

---

## Mistake 2

I focused on SQL syntax before understanding relationships.

Correction:

Identify the relationship first.

Write SQL second.

---

## Mistake 3

I sometimes confuse the direction of the bridge.

Reminder:

Ask:

Who stores the reference?

Employee stores manager_id.

Manager owns emp_id.

Therefore:

e.manager_id = m.emp_id

---

# Interview Thinking

Never memorize JOIN queries.

Instead ask:

What is connected to what?

Example:

Employee → Department

Employee → Manager

Order → Customer

Student → Course

The bridge answers the JOIN automatically.

---

# Mentor's Advice

A JOIN is not magic.

It is simply SQL following a relationship created by the database designer.

Understand the relationship.

The SQL will follow naturally.
