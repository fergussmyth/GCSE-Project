
def sign_up():
    global name
    global password

    previous_user = input("Are you a previous user? [Y/N]").upper()

    if previous_user == "Y":
        login()


    name = input('Enter your name:')
    password = input('Enter your password')

    combine = (name,password)

    add_info = open("users.txt", "a+")
    add_info.write("\n")
    add_info.write(str(combine))



def login():

    user_open = open("users.txt", "r")

    print("\n")
    username = input("Please enter your username")
    password_enter = input("Please enter your password")

    if username and password_enter in user_open:
        print("Welcome!")

    else:
        print("\n", "Incorrect username or password!")
        login()
