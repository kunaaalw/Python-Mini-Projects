print('Welcome to my computer quiz!')

playing = input('Do you want to play?: ').lower()

if playing != 'yes':
    quit()

print("Okay! Lets Play!")

# keeping the score
score = 0

# Question 1
answer1 = input('What does CPU stand for?: ').lower()
if answer1 == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

# Question 2
answer2 = input('What does GPU stand for?: ').lower()
if answer2 == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

    # Question 3
answer3 = input('What does RAM stand for?: ').lower()
if answer3 == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

 # Question 4
answer4 = input('What does PSU stand for?: ').lower()
if answer4 == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print(f'You got {score} questions correct')
print('You got', str(score/4 * 100), "%.")
