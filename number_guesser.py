import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter number that is greater than zero")
        quit()

else:
    print("Please enter a valid number")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number")
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You guessed a higher number')
    else:
        print('You guessed a lower number')

print(f'You guessed the number in {guesses} tries.')
