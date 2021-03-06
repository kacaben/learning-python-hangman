# Project #2: Hangman

from random import randint
import os


words = ["abruptly", "awkward", "bagpipes", "bandwagon", "beekeeper", "bikini", "blizzard", "boggle", "bookworm",
         "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb",
         "cockiness", "croquet", "curacao", "daiquiri", "disavow", "dizzying", "dwarves", "embezzle", "espionage",
         "euouae", "exodus", "faking", "fishhook", "fixable", "flapjack", "flopping", "fluffiness", "foxglove",
         "frazzled", "frizzled", "fuchsia", "galaxy", "galvanize", "gazebo", "glowworm", "gnarly", "gnostic", "gossip",
         "grogginess", "haphazard", "hyphen", "iatrogenic", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest",
         "jigsaw", "jiujitsu", "jogging", "joking", "jovial", "joyful", "jukebox", "keyhole", "kilobyte", "kitsch",
         "kiwifruit", "knapsack", "larynx", "lengths", "luxury", "megahertz", "microwave", "mnemonic", "mystify",
         "naphtha", "nightclub", "nowadays", "numbskull", "oxidize", "oxygen", "peekaboo", "phlegm", "pneumonia",
         "puzzling", "quartz", "quixotic", "quizzes", "razzmatazz", "rickshaw", "schnapps", "strength", "strengths",
         "stronghold", "stymied", "syndrome", "thriftless", "thumbscrew", "transcript", "transgress", "transplant",
         "triphthong", "twelfths", "unknown", "unworthy", "vaporize", "vortex", "voyeurism", "walkway", "wellspring",
         "whizzing", "whomever", "witchcraft", "wristwatch", "xylophone", "yachtsman", "youthful", "zigzagging"]


# drawing the hangman row by row
drawRows = ["-----", "|   |", "|   o", "|  /|\\", "|  / \\", "|"]
# each error has a specific row and position, where the drawing stops
rowPos = [[-1, 1], [0, 6], [1, 6], [2, 6], [3, 4], [3, 5], [3, 6], [4, 4], [4, 6]]


def drawHang(row, pos):
    if row >= 0:
        for i in range(6):
            if i < row:
                print(drawRows[i])  # hangman from the previous errors
            elif i == row:
                print(drawRows[i][:pos])  # actual position from the current error
            else:
                print(drawRows[i][:1])  # the first column only
    else:
        for i in range(1, 6):
            print(drawRows[i][:1])  # first error draws a column


def showWord(sh_word, sh_letters):
    sh_word = sh_word
    sh_letters = sh_letters
    show_word = ""

    for char in sh_word:
        if char in sh_letters:
            show_word += char
        else:
            show_word += "-"
    print("\nThe game word is: ", show_word)
    return show_word


def gameCheck(visible_w, errs):
    visible_w = visible_w
    errs = errs
    dash = "-"

    if dash not in visible_w:
        print("You won the game!")
        return False

    if errs == 8:
        print("Sorry, you lost. Game over.")
        return False


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


letters = []
incorrect_letters = []
game = True
err = 2  # you can set to 0 and start drawing the gallows with each error
solo = " "

print("Hangman word game")

while solo == " ":
    solo = input("Select [1] player or [2] players game: ")

    if solo == "1":
        word = words[randint(0, len(words) - 1)]
    elif solo == "2":
        word = input("Player 1, enter the game word: ")
    else:
        solo = " "


screen_clear()

while game:
    letter = input("Enter a letter. Type 0 if you want to quit: ").lower()
    screen_clear()
    if letter == "0":
        print("OK, Bye.")
        break
    else:
        letters.append(letter)

        if letter not in word:
            incorrect_letters.append(letter)
            print("\nSorry,", letter, "is a wrong letter.")
            err += 1

    if incorrect_letters:
        print("\nWrong letters: ", *incorrect_letters)
    print("\n")
    drawHang(rowPos[err][0], rowPos[err][1])
    visible_word = showWord(word, letters)
    print("\n")

    if gameCheck(visible_word, err) is False:
        game = False


print("Thank you for playing")

wait = input()  # to leave the window open
