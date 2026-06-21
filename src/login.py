class Login:
    def authenticate(self, username, password):
        if username == "admin" and password == "admin123":
            return True
        return False
