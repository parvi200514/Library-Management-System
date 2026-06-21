# Entity Relationship Diagram

## Entities

### Admin
- admin_id (PK)
- username
- password
- full_name

### Books
- book_id (PK)
- title
- author
- publisher
- category
- isbn
- quantity
- available_quantity

### Students
- student_id (PK)
- student_name
- course
- semester
- phone
- email

### Transactions
- transaction_id (PK)
- student_id (FK)
- book_id (FK)
- issue_date
- due_date
- return_date
- status

## Relationships

Student (1) -------- (M) Transactions

Book (1) -------- (M) Transactions
