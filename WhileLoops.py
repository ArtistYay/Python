import random
#1. What do I want to repeat?
# -> guesses
#2. What do I want to change each time?
# -> The number
#3. How long should we repeat?
# -> 3 times

print('Guessing game!')

num = random.randint(1, 20)
guess = '' #User will input number so leave this variable blank.
guess_number = 0
guess = int(input(f'Guess a number between 1-20: '))

while guess_number < 3:
    if guess != num: #If the user guess number is not equal 
        guess_number += 1 #then the guess number, which started off at 0, is added by 1.
        if guess > num:
            guess = int(input(f'{guess} is to high - try again: ')) #If the user guessed to high the computer will let them know.
        else:
            guess = int(input(f'{guess} is to low - try again: ')) #If the user guessed to low the computer will let them know.
    if guess == num:
        print(f'Congradulations! You guessed {guess} correctly!')

if guess != num: 
    print(f'Sorry you lose :( it was {num}') #Once the user run out of gueses the computer will let them know the number.