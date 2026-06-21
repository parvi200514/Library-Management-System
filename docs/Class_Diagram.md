# Class Diagram

## Admin

Attributes:
- admin_id
- username
- password
- full_name

Methods:
- login()
- logout()

---

## Book

Attributes:
- book_id
- title
- author
- publisher
- category
- isbn
- quantity
- available_quantity

Methods:
- add_book()
- update_book()
- delete_book()
- search_book()

---

## Student

Attributes:
- student_id
- student_name
- course
- semester
- phone
- email

Methods:
- add_student()
- update_student()
- delete_student()
- search_student()

---

## Transaction

Attributes:
- transaction_id
- student_id
- book_id
- issue_date
- due_date
- return_date
- status

Methods:
- issue_book()
- return_book()
- generate_report()

Relationships:

Student → Transaction

Book → Transaction
