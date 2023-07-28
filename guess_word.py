import os


def start():
    global word_input
    while True:
        word_input = input('Player 1, enter your word: ')
        if word_input.isalpha() and len(word_input) > 0:
            return word_input.lower()
        else:
            print('Invalid input. Please enter a valid word.')


word_input = start()
os.system('cls')

used_letters = []
letters_word = list(word_input.lower())
word_progress = list('*' * int(len(letters_word)))

print('Player 2,there are', len(letters_word), 'letters in the word:')
print(*word_progress, sep='')


def game():
    letter_input = input('Enter your letter:').lower()

    if letter_input in used_letters:
        return print('This letter is already guessed.')
    else:
        os.system('cls')
        if letter_input in letters_word:
            used_letters.append(letter_input)
            for index, elem in enumerate(letters_word):
                if letter_input == elem:
                    word_progress[index] = elem
            print("The word is ", *word_progress, sep='')
            return print(f"You guessed a letter {letter_input}.")

        else:
            used_letters.append(letter_input)
            print("The word is ", *word_progress, sep='')
            return print('Letter  "', letter_input, '"  is not correct.')


while "*" in word_progress:
    game()
else:
    os.system('cls')
    print("Congratulations, you won!\nGuessed word was:", word_input)
    input()
