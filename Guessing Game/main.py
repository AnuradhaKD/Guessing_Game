import random

number = random.randint(1, 20)

player_name = input("Enter your name? ")
num_of_guesses = 0

print('OK '+ player_name+ ' I am Guessing a number between 1 and 20:')

while num_of_guesses < 5:
    guess = int(input('your guess - '))
    num_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
    
if guess == number:
    print('You guessed!!!🤗🤗🤗 the number guessed in ' + str(num_of_guesses) + ' tries!')
else:
    print('You did not guess the number 😢😢😢😢, The number was ' + str(number))
    
#     ~AkD~
