import random

computer_word = random.choice(open('words.txt', "r").read().split())
print(computer_word)
# read_file=open_file.read()
# computer_word=random.choice(read_file)
invalid_guess = []
incorrect_guess = []
correct_guess = []
# invalid_guess2 = []
# ☑️ sets limit to number of tries
# 2.1 identifies more than one letter being input
# 2.2 tells user input is invalid if the more than one letter is input


# create a board based on letters in word
def game_board(word, correct_guess):
    letters_in_word_board = ""
    for letter in word:
        if letter in correct_guess:
            letters_in_word_board += letter + " "
        else:
            letters_in_word_board += "_ "
    return letters_in_word_board


def invalid_input(guess):
    # board = game_board(computer_word, correct_guess)
    if len(guess) > 1:
        print('Invalid guess. Please enter only ONE letter.')
        print("")
        invalid_guess.append(guess)
        print(f"Invalid: {invalid_guess}")
        guess = input("Guess a letter: ")
        return invalid_input(guess)
    elif len(guess) == 0:
        print('Invalid guess. Please enter a letter.')
        print("")
        invalid_guess.append(guess)
        print(f"Invalid: {invalid_guess}")
        guess = input("Guess a letter: ")
        return invalid_input(guess)
    else:
        print(f'GUESS: {guess}')
        return guess


def duplicate_input(guess):
    if guess in incorrect_guess or guess in correct_guess:
        print(f'Incorrect Guess: {incorrect_guess}')
        print(f'Correct Guess: {correct_guess}')
        print(f'Guess: {guess}')
        print('You have already tried that letter!')
        guess = input("Guess a letter: ")
        duplicate_input(guess)
    else:
        return guess


def play_game(word):
    # invalid_guess = []
    # incorrect_guess = []
    # correct_guess = []
    word_length = len(word)  # calculates the length of the random word
    # ☑️ 1.1 tells player how many letters are in the word
    print(f'The word has {word_length} letters')
    # ☑️ 1.2 Tells user to give one guess per round
    print("You get one guess per round and 8 total guesses.")
    # letters_in_word = ["_" for letter in word]
    print("")
    tries = 8
    board = game_board(computer_word, correct_guess)
    print(board)
    # first_round_board(computer_word)
    # letters_in_word = [game_board for letter in computer_word]
    while tries > 0:  # while loop says keep going until run out of tries
        # letters_in_word = ["_" for letter in word]
        # print(letters_in_word)
        # print("")
        # board = game_board(computer_word, correct_guess)
        # print(correct_guess)
        # print(board)
        print(f'Incorrect letters: {incorrect_guess}')
        print("")
        guess = input("Guess a letter: ")
        print("")
        guess = invalid_input(guess)
        guess = duplicate_input(guess)
        # print(f'Guess: {guess}')
        if guess not in word:
            tries -= 1
            print(f'Oof! {tries} guesses left.')
            incorrect_guess.append(guess)
            print("")
            if tries == 0:
                print('Darn! You have used up all of your guesses.')
                print("")
                play_again = input('Play again? y/n ')
                print("")
                if play_again == "y":
                    new_computer_word = random.choice(
                        open('words.txt', "r").read().split())
                    print(new_computer_word)
                    return play_game(new_computer_word)
        else:
            # 3.1 identifies correct letter in word
            # 3.2 lets the user know if their guess appears in the secret word
            print(f'Nice! You still have {tries} guesses left.')
            correct_guess.append(guess)
            print("")  # adds to guess
            board = game_board(computer_word, correct_guess)
            print(f'Correct: {correct_guess}')
            print(board)
            # for i in range(len(word)):
            #     if guess == word[i]:
            #         word[i] = word
            #         board
            #         print("")
            test_board = game_board(computer_word, correct_guess)
            if "_ " not in test_board:
                print("You Win!")
                print("")
                play_again = input('Play again? y/n ')
                print("")
                if play_again == "y":
                    new_computer_word = random.choice(
                        open('words.txt', "r").read().split())
                    print(new_computer_word)
                    return play_game(new_computer_word)

        # return
            # print(f'The word has {word_length} letters')
            # print(letters_in_word)


play_game(computer_word)


if __name__ == "__main__":
    play_game()
