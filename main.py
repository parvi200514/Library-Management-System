from src.login import Login

print("Library Management System")

login = Login()

if login.authenticate("admin", "admin123"):
    print("Login Successful")
else:
    print("Login Failed")
