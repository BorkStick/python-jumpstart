from mimetypes import guess_type
import random


print("----------------")
print("Guess the Number")
print("----------------")
print()

the_number = random.randint(0, 10)
guess = -1
attempts = 0



# debug
print("Answer: ")
print(the_number)



while guess != the_number:
    guess_text = input('Guess the number between 0 nad 10: ')
    guess = int(guess_text)
    #attempts =+ 1 
    if guess < the_number:
        print(f'{guess} is too low')
        attempts += 1 
    elif guess > the_number:
        print(f'{guess} is too too high')
        attempts += 1 
    else:
        attempts += 1 
        print("Guess: ")
        print(guess)
        print("Attempts: ")
        print(attempts)
        print('YOU WIN')


#print("GAME OVER MAN")
