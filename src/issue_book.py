from datetime import date, timedelta


class IssueBook:

    def issue(self, student_id, book_id):

        transaction = {
            "student_id": student_id,
            "book_id": book_id,
            "issue_date": str(date.today()),
            "due_date": str(date.today() + timedelta(days=14)),
            "status": "Issued"
        }

        return transaction
