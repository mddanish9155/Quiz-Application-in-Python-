def register():
    try:
        with open("users.txt", "a") as file:
            username = input("Enter username: ")
            password = input("Enter password: ")
            file.write(f"{username},{password}\n")
            print("Registration successful!")
    except Exception as e:
        print("Error during registration:", e)

if __name__ == "__main__":
    register()
