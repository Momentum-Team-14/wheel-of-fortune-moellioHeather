import random

computer_word = random.choice(open('words.txt', "r").read().split())
print(computer_word)
# read_file=open_file.read()
# computer_word=random.choice(read_file)

# 2.1 identifies more than one letter being input
# 2.2 tells user input is invalid if the more than one letter is input


def play_game(word):
    # create a board based on letters in word
    letters_in_word = ["_" for letter in word]
    word_length = len(word)  # calculates the length of the random word
    incorrect_guess = []
    correct_guess = []
    tries = 8  # ☑️ sets limit to number of tries
    while tries > 0:  # while loop says keep going until run out of tries
        # ☑️ 1.1 tells player how many letters are in the word
        print(f'The word has {word_length} letters')
        print(letters_in_word)
        print("You get one guess per round and 8 total guesses.")
        print("")
        # ☑️ 1.2 Tells user to give one guess per round
        guess = input("Guess a letter: ")
        guess_length = len(guess)
        break
        if guess_length > 1:
            print('Invalid guess. Please enter only one letter.')
        elif guess in incorrect_guess or correct_guess:
            print('You have already tried that letter!')
        elif guess not in word:
            tries -= 1
            print(f'Oof! {tries} guesses left.')
            incorrect_guess.append(guess)
            print(f'Wrong letters: {incorrect_guess}')
            if tries == 0:
                print('Darn! You have used up all of your guesses.')
            # print('Play again? (y/n)?')
            else:
                # 3.1 identifies correct letter in word
                # 3.2 lets the user know if their guess appears in the secret word
                for i in range(len(letters_in_word)):
                    if guess == word[i]:
                        letters_in_word[i] = guess
                        correct_guess.append(guess)  # adds to guess
                        print(f'Nice! You still have {tries} guesses left.')

                    # print(f'The word has {word_length} letters')
                    # print(letters_in_word)


play_game(computer_word)


if __name__ == "__main__":
    play_game()
