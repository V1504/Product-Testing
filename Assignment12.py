def Login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Invalid credentials.")
Login()