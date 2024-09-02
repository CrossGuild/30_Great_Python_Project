import random

def roll_dice(amount: int = 1):
    while True:
        try:
            amount = int(input("How many dice do you want to roll? "))

            if type(amount) != int:
                raise ValueError
            else:
                rolls: list[int] = []
                for i in range(amount):
                    rand_roll = random.randint(1, 6)
                    rolls.append(rand_roll)
                    print(*rolls, sep = ',')
                break
        except ValueError:
            print("Enter an integer")
            break

if __name__ == '__main__':
    roll_dice()
