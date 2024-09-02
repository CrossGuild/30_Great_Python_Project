from random import choice
from symbol import continue_stmt

def run_game():
    word: str = choice(['apple', 'orange', 'pear'])

    username: str = input('What is your name? :')
    print(f'Welcome to hangman, {username}!')

    #Setup
    guessed: str = ''
    tries: int = 5

    while tries > 0:
        blanks: int = 0
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='\n')
            else:
                print('_', end=' ')
                blanks += 1
        print() # Adds a blank line

        if blanks == 0:
            print('You got it!')
            break

        guess: str = input('Guess a letter: ')

        if guess in guessed:
            print(f'You already guessed {guess}!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong, {tries} tries remaining.")

            if tries == 0:
                print("No more tries remaining.. You lose.")
                break

if __name__ == '__main__':
    run_game()

