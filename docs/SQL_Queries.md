# SQL Queries Used in Project

## View All Books

SELECT * FROM books;

---

## Search Book

SELECT * FROM books
WHERE title='Python Basics';

---

## View Students

SELECT * FROM students;

---

## View Transactions

SELECT * FROM transactions;

---

## Issued Books

SELECT * FROM transactions
WHERE status='Issued';

---

## Returned Books

SELECT * FROM transactions
WHERE status='Returned';

---

## Available Books

SELECT *
FROM books
WHERE available_quantity > 0;
