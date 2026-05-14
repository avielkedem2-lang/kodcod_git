import random
print("================================")
print("Welcome to the Hanged Man game")
print("================================")
print("")
print("")


def get_word_from_the_bank():
    word_bank = [
    "Galaxy", "Python", "Mountain", "River", "Keyboard", 
    "Ocean", "Software", "Cloud", "Algorithm", "Coffee", 
    "Forest", "Sunset", "Database", "Laptop", "Science"]
    word = random.choice(word_bank)
    word = "aviel"
    return word




def result_guess(list_words, word):
    print_word = ""
    for char in word.lower():
        if char in list_words:
            print_word += char
        else:
            print_word += "_"
    return print_word




def show_status_game(the_guess_word, guesses, list_words):
    print(f"Word:{result_guess(list_words, the_guess_word)}")
    print(f"You have a {guesses} guesses!")
    print(f"You already guessed: {list_words}")
    print("")
    print("")
    print("")



def is_cher_in_word(user_choice, the_guess_word, my_bank_words):
    global guesses
    if user_choice.lower() in the_guess_word.lower():
        print("wonderful!!! \U0001F600")
        checke_guess = result_guess(my_bank_words, the_guess_word)
        if "_" not in checke_guess or user_choice.lower() == the_guess_word.lower():
            print(f"Congratulations, you found the word: {the_guess_word} \U0001F3AF")
            flag_game_on =False 
            return flag_game_on
        else:
            flag_game_on = True
            return flag_game_on

    else:
        guesses -= 1
        print("You guessed wrong! \u274C")
        if guesses == 0:
            print("You're out of guesses. You're disqualified!!! \U0001F480")
            flag_game_on = False
            return flag_game_on
        else:
            flag_game_on = True
            return flag_game_on





the_guess_word = get_word_from_the_bank()
guesses = 8
my_bank_words = []
flag_game_on = True



while flag_game_on:
    show_status_game(the_guess_word, guesses, my_bank_words)

    user_choice = input("Choose a letter or the word: ")
    if not user_choice.isalpha():
        print("you need to input letter or word!")
        continue
    
    if user_choice.lower() not in my_bank_words:
        my_bank_words.append(user_choice.lower())
    
        flag_game_on = is_cher_in_word(user_choice, the_guess_word, my_bank_words)
    
            

        

