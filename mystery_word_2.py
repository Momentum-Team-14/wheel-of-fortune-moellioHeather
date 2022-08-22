import random

computer_word = random.choice(open('words.txt', "r").read().split())
print(computer_word)
# read_file=open_file.read()
# computer_word=random.choice(read_file)
incorrect_guess = []
correct_guess = []
invalid_guess1 = []
invalid_guess2 = []
# ☑️ sets limit to number of tries
# 2.1 identifies more than one letter being input
# 2.2 tells user input is invalid if the more than one letter is input


# def first_round_board(word):
#     word_length = len(word)  # calculates the length of the random word
#     # ☑️ 1.1 tells player how many letters are in the word
#     print(f'The word has {word_length} letters')
#     # ☑️ 1.2 Tells user to give one guess per round
#     print("You get one guess per round and 8 total guesses.")
#     letters_in_word = ["_" for letter in word]
#     print(letters_in_word)
#     print("")


# create a board based on letters in word
def game_board(word, correct_guess):
    letters_in_word_board = ["_" for letter in word]
    for i in range(len(word)):
        if word[i] in correct_guess:
            letters_in_word_board[i] = word[i]
    word_board = " ".join(letters_in_word_board)
    return word_board


def invalid_input(guess):
    if len(guess) > 1:
        print('Invalid guess. Please enter only ONE letter.')
        print("")
        guess = input("Guess a letter: ")
        return invalid_input(guess)
    elif len(guess) == 0 or guess == "":
        print('Invalid guess. Please enter a letter.')
        print("")
        guess = input("Guess a letter: ")
        return invalid_input(guess)
    invalid_guess1.append(guess)
    return guess


def duplicate_input(guess):
    if guess in incorrect_guess or correct_guess:
        print('You have already tried that letter!')
        guess = input("Guess a letter: ")
        return duplicate_input(guess)
    return guess


def play_game(word):
    word_length = len(word)  # calculates the length of the random word
    # ☑️ 1.1 tells player how many letters are in the word
    print(f'The word has {word_length} letters')
    # ☑️ 1.2 Tells user to give one guess per round
    print("You get one guess per round and 8 total guesses.")
    # letters_in_word = ["_" for letter in word]
    print("")
    tries = 8
    # first_round_board(computer_word)
    # letters_in_word = [game_board for letter in computer_word]
    board = game_board(computer_word, correct_guess)
    print(board)
    while tries > 0:  # while loop says keep going until run out of tries
        # letters_in_word = ["_" for letter in word]
        # print(letters_in_word)
        # print("")

        print(f'Incorrect letters: {incorrect_guess}')
        print("")
        guess = input("Guess a letter: ")
        print("")
        # invalid_input(guess)
        # duplicate_input(guess)
        if guess not in word:
            tries -= 1
            print(f'Oof! {tries} guesses left.')
            incorrect_guess.append(guess)
            print("")
            if tries == 0:
                print('Darn! You have used up all of your guesses.')
                print("")
                print('Play again? (y/n)?')
        else:
                # 3.1 identifies correct letter in word
                # 3.2 lets the user know if their guess appears in the secret word
            print(f'Nice! You still have {tries} guesses left.')
            # for i in range(len(word)):
            #     if guess == word[i]:
            #         # word[i] = word
            correct_guess.append(guess)  # adds to guess
            print("")
                # print(f"{board}\n")
            board = game_board(computer_word, correct_guess)
            print(correct_guess)
            print(board)
            if "_" not in board:
                print("You Win!")
                return
                # print(f'The word has {word_length} letters')
                # print(letters_in_word)


play_game(computer_word)


if __name__ == "__main__":
    play_game()
