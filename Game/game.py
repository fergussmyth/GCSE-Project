import random as rd
import hashlib
games

def get_info():

    info = open(r"C:\Users\fergg\.vscode\GCSE-Project\Game\test.txt", "r")
    songs = info.readlines()
    title_list = []

    for i in range(len(songs)):
        title_list.append(songs[i].strip('\n'))

    while games == True:
        choice = rd.choice(title_list)
        artist, song = choice.split(',')

        songs = song.split()
        letter = [word[0] for word in songs]

        print("\n")
        print("Artist:", artist)
        print("Song:", " ".join(letter))

    song_main = choice.split(",")

    games = True
    points = 0
    attempt = 4
   

    while games == True:

        guess = input("Please enter your guess:").upper()
        
        if guess == song_main[1]:
            points += 3
            print("Well Done, you have", points, "points!")
            

        if guess != song_main[1]:
            points -= 1
            attempt -= 1
            print("You have", points, "points! \n")
            print("You have", attempt, "attempts remaining! \n")

        if attempt == 0:
            points -= 1
            print("You have 0 attempts remaining\nGame Over")
            games = False


def sign_up():
    username = input("Please enter a username:")
    password = input("Please enter a password:")
    conf_password = input("Please enter your password again:")

    if conf_password == password:
        encode_pass = conf_password.encode()
        hash1 = hashlib.md5(encode_pass).hexdigest()

    else: 
        print("Passwords do not match")

    with open("users.txt", "w") as f:
        f.write(username + ", " + hash1)
    f.close()
    print("You have registered successfully!")
    sign_in()
    
def sign_in():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    authenticate = password.encode()
    authenticate_hash = hashlib.md5(authenticate).hexdigest()

    with open("users.txt", "r") as f:
        stored_username, stored_password = f.read().split(", ")
        f.close()
    
    if username == stored_username and authenticate_hash == stored_password:
        print("Logged in successfully!")
        get_info()
    else:
        print("Login failed! \n","Please try again")
        sign_in()

while 1:
    print("******* Login System *******")
    print("1. Signup \n2. Login \n3. Exit")
    
    choice = int(input("Please select an option: "))

    if choice == 1:
        sign_up()
        break
    elif choice == 2:
        sign_in()
        break
    elif choice == 3:
        break
    else:
        print("That is not an option:")



