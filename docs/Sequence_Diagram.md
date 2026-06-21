# Sequence Diagram

Librarian
    |
    | Login
    v
System
    |
    | Validate User
    v
Database
    |
    | Success
    v
System
    |
Issue Book Request
    |
Check Availability
    |
Update Transaction
    |
Return Confirmation
    |
Librarian
