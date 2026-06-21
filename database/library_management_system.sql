-- ADMIN DATA

INSERT INTO admin(username,password,full_name)
VALUES
('admin','admin123','Library Administrator');


-- SAMPLE BOOKS

INSERT INTO books
(title,author,publisher,category,isbn,quantity,available_quantity)
VALUES
('Python Basics','E Balagurusamy','McGraw Hill','Programming','ISBN1001',10,10),

('Database Systems','Henry Korth','Pearson','Database','ISBN1002',8,8),

('Software Engineering','Roger Pressman','McGraw Hill','Software','ISBN1003',12,12),

('Computer Networks','Andrew Tanenbaum','Pearson','Networking','ISBN1004',5,5),

('Operating Systems','Galvin','Wiley','System','ISBN1005',7,7);


-- SAMPLE STUDENTS

INSERT INTO students
(student_name,course,semester,phone,email)
VALUES
('Rahul Sharma','BCA',6,'9876543210','rahul@example.com'),

('Priya Verma','BCA',6,'9876543211','priya@example.com'),

('Aman Gupta','BCA',5,'9876543212','aman@example.com'),

('Neha Singh','BCA',4,'9876543213','neha@example.com');


-- SAMPLE TRANSACTIONS

INSERT INTO transactions
(student_id,book_id,issue_date,due_date,return_date,status)
VALUES
(1,1,'2026-01-10','2026-01-24',NULL,'Issued'),

(2,2,'2026-01-05','2026-01-19','2026-01-18','Returned');
