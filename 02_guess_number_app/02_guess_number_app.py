from mimetypes import guess_type
import random


print("----------------")
print("Guess the Number")
print("----------------")
print()

the_number = random.randint(0, 100)
guess = -1



# debug
print("Answer: ")
print(the_number)



while guess != the_number:
    guess_text = input('Guess the number between 0 nad 100: ')
    guess = int(guess_text)
    
    if guess < the_number:
        print("too low")
    elif guess > the_number:
        print("to0 high")
    else:
        print('you win')


print("GAME OVER MAN")
print("Guess: ")
print(guess)