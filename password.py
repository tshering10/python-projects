print("Welcome to the password manager. ")
def view():
    with open("details.txt", "r") as f:
        lines = f.readlines()
        if lines:
            for line in lines:
                data = line.rstrip()
                username, password = data.split(",")
                print(f"Username: {username}")
                print(f"Password: {password}")
        else:
            print("No details saved yet.")
def add():
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if username and pwd:
        with open("details.txt", "a") as f:
            f.write("\n")
            f.write(username + "," + pwd )
            print("Added your Credentials successfully!!")
    else:
        print("Username and password required!!!!")
    
while True:
    user_input = input("""
    1. Type add for adding password
    2. Type view for viewing password
    3. Type q for exixting
    """)
    if user_input.lower() == "add":
        add()
    elif user_input.lower() == "view":
        view()
    elif user_input.lower() == "q":
        print("Thanks!!")
        break
    else:
        print("Invalid input. Please choose a valid option.")
    