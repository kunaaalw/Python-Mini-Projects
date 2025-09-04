import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print('Enter a valid input')
        continue

    random.number = random.randint(0, 2)
    # rock: 0, paper:1, scissors: 2
    computer_input = options[random.number]
    print(f'Computer picked {computer_input}.')

    if user_input == 'rock' and computer_input == 'scissors':
        print('You Won!')
        user_wins += 1

    elif user_input == 'paper' and computer_input == 'rock':
        print('You Won!')
        user_wins += 1

    elif user_input == 'scissors' and computer_input == 'paper':
        print('You Won!')
        user_wins += 1

    else:
        print('You Lost!')
        computer_wins += 1

print(f'You won {user_wins} times. '
      f'The Computer won {computer_wins} times.')
print('Thank you for playing!')
