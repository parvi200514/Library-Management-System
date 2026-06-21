from datetime import date


class ReturnBook:

    def return_book(self, transaction_id):

        return {
            "transaction_id": transaction_id,
            "return_date": str(date.today()),
            "status": "Returned"
        }
