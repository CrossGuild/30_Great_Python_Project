from random import randint

def num_guessing_game():
    lower_num : int = 1
    higher_num : int = 10
    ran_num = randint(lower_num, higher_num)
    print(ran_num)
    while True:
        try:
            guess: int = int(input("Guess the number in the range from 1 to 10: "))
            if guess > ran_num:
                print("Too Big")
            elif guess < ran_num:
                print("Too Small")
            else:
                print("You are right!")
                break

        except ValueError as error:
            print("Please enter a valid number.")

        finally:
            print("You enetered a number anyway, GJ!")

if __name__ == '__main__':
    ngg =  num_guessing_game()
    ngg

