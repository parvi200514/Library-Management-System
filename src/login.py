class Login:

    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD = "admin123"

    def authenticate(self, username, password):

        if (
            username == self.DEFAULT_USERNAME
            and password == self.DEFAULT_PASSWORD
        ):
            return True

        return False
