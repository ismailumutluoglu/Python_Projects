# SAYI TAHMIN ETME OYUNU (NUMBER GUESS GAME)

import random

print("HI!  WELCOME TO  THE GAME, THIS IS A NUMBER GUESSING NAME.\YOU GOT 10 CHANCES TO GUESS THE NUMBER. LET'S START THE GAME")

numberToGuess = random.randrange(100)

chances = 10

counter = 0

while counter < chances:

    counter = counter +  1
    myGuess = int(input('Please Enter your Guess : '))

    if myGuess == numberToGuess:
        print(f'The number is {numberToGuess} and you found it right  in the {counter} attempt !!')
        break

    elif counter >= chances and myGuess != numberToGuess:
        print(f'Oops sorry, The number is {numberToGuess} better luck next time')

    elif myGuess > numberToGuess:
        print('Your guess is higher ')

    elif myGuess < numberToGuess:
        print('Your guess is lesser')