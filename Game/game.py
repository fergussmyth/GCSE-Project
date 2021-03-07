import random as rd
from sign_up import *

sign_up()
login()

def get_info():
    global songs
    global choice
    global song_main

    info = open("artist-song.txt", "r")
    songs = info.readlines()
    title_list = []

    for i in range(len(songs)):
        title_list.append(songs[i].strip('\n'))

    choice = rd.choice(title_list)
    artist, song = choice.split(',')

    songs = song.split()
    letter = [word[0] for word in songs]

    print("\n")
    print("Artist:", artist)
    print("Song:", " ".join(letter))

    song_main = choice.split(",")


def game():
    games = True
    points = 0
    attempt = 0

    while games:
        guess = input("Please enter your guess:").upper()

        if guess == song_main[1]:
            points += 3
            print("Well Done, you have", points, "points!")
            get_info()

        if guess != song_main[1]:
            points += 1
            attempt += 1

        if attempt == 2:
            points -= 1
            score_add = open("scores.txt", "a+")
            score_add.write("\n")
            score_add.write(str(points))
            score_add.close()
            games = False



get_info()
game()
