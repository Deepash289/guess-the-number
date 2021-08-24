from random import randint
secret = randint(0, 10)
guess_range = range(0,11)
guess = None
count = 1

while guess != secret:
    guess = input('what is your guess from (0-10): ')
    if guess.isdigit():
        guess = int(guess)
        if guess not in guess_range:
            print('Please put a number between (0-10)')
        else:
            if guess > secret:
                print("Lower")
                count += 1
            elif guess < secret:
                print("Higher")
                count += 1
            else:
                print(f'good job! you got the right answer\nIt took you: {count} tries.')
    else:
        print('That is not a number')