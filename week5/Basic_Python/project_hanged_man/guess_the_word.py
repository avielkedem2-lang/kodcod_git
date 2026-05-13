import random
print("================================")
print("Welcome to the Hanged Man game")
print("================================")
print("")
print("")


def choosing_word():
    word_bank = [
    "Galaxy", "Python", "Mountain", "River", "Keyboard", 
    "Ocean", "Software", "Cloud", "Algorithm", "Coffee", 
    "Forest", "Sunset", "Database", "Laptop", "Science"]
    word = random.choice(word_bank)
    return word




def status_word(list_words, word):
    print_word = ""
    for char in word.lower():
        if char in list_words:
            print_word += char
        else:
            print_word += "_"
    return print_word



the_guess_word = choosing_word()
guesses = 8
list_words = []
flag_game_on = True
def show_status_game(status_word, the_guess_word, guesses, list_words):
    print(f"Word:{status_word(list_words, the_guess_word)}")
    print(f"You have a {guesses} guesses!")
    print(f"You already guessed: {list_words}")
    print("")
    print("")
    print("")

while flag_game_on:
    show_status_game(status_word, the_guess_word, guesses, list_words)
    choice = input("Choose a letter: ")
    list_words.append(choice)
    if choice in the_guess_word:
        print("wonderful!!!")
        checke_guess = status_word(list_words, the_guess_word)
        if "_" not in checke_guess:
            print(f"Congratulations, you found the word: {the_guess_word}")
            flag_game_on =False 

    else:
        guesses -= 1
        print("You guessed wrong!")
        if guesses == 0:
            print("You're out of guesses. You're disqualified!!!")
            flag_game_on = False
            

        

