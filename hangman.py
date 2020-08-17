# Write your code here
import random
import string

menu_choice = ""

print("H A N G M A N")
while menu_choice != "play" and menu_choice != "exit":
    menu_choice = input('Type "play" to play the game, "exit" to quit: ')

while menu_choice != "exit":

    word_list = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    word = random.choice(word_list)
    guess_display = "-" * len(word)
    guess = ""
    tries = 0
    successful_letters = set()
    attempted_letters = set()
    letters_in_word = set(word)
    win = False

    while tries != 8:
        print("\n" + guess_display)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif guess in attempted_letters:
            print("You already typed this letter")
        elif guess in word and guess not in successful_letters:
            successful_letters.add(guess)
            attempted_letters.add(guess)
            for j, letter in enumerate(guess_display):
                if word[j] == guess:
                    guess_display_list = list(guess_display)
                    guess_display_list[j] = guess
                    guess_display = "".join(guess_display_list)
            if len(successful_letters) == len(letters_in_word):
                win = True
                break
        else:
            attempted_letters.add(guess)
            tries += 1
            print("No such letter in the word")

    if win:
        print("You guessed the word!\nYou survived!")
    else:
        print("You are hanged!")

    menu_choice = ""
    while menu_choice != "play" and menu_choice != "exit":
        menu_choice = input('Type "play" to play the game, "exit" to quit: ')