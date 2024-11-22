def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    return True
        print("Invalid username or password.")
        return False
    except FileNotFoundError:
        print("User database not found. Please register first.")
        return False
    except Exception as e:
        print("Error during login:", e)
        return False

if __name__ == "__main__":
    login()
