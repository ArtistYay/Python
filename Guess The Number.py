import random 

def guess(x): #Defined guess and make 'x' the parameter
    random_number = random.randiant(1, x) 
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')


def computer_guess(x):
    low = 1
    high = x  