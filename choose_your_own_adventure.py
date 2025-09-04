name = input("Please enter your name: ")
print(f'Welcome {name} to this adventure!')

answer = input(
    'You are on a dirt road, it has come to an end and you can go LEFT or RIGHT. Which way would you like to go?: ').lower()
if answer == 'left':
    answer = input(
        'You come to a river, and you can walk around it or swim accorss it. Type WALK to walk around and SWIM to swim accross: ').lower()
    if answer == "swim":
        print(
            "You swam accross the river and were eaten by an aligator. You lost the game!")
    elif answer == "walk":
        print(
            "You walk for many miles, an eventually ran out of water and you lost the game.")
    else:
        print('Not a valid opiton. You lose!')
elif answer == 'right':
    answer = input(
        'You come to a bridge , it looks wobbly, do you want to cross it or head back (CROSS / BACK)?: ').lower()
    if answer == "back":
        print(
            "You go back and lose!")
    elif answer == "cross":
        answer = input(
            "You crossed the bridge and met a stranger. Do you talk to them (YES / NO)?: ").lower()
        if answer == "yes":
            print('You talk to the stranger and they get back you to city. YOU WIN!')
        elif answer == 'no':
            print("You ignore the stranger and get lost and eventually die. You lose!")
        else:
            print('Not a valid opiton. You lose!')
    else:
        print('Not a valid opiton. You lose!')
else:
    print('Not a valid option. You lose!')

print(f"Thank you {name} for playing this game!")
