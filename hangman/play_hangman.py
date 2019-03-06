import hangman
from hangman import Hangman
import random

words=['pizza', 'noodles', 'crossword', 'squid', 'monkey', 'alive', 'telephone']
random.seed()

ask_answer=''
while not len(ask_answer)==1:
    ask_answer = input("Do you want to play a game? (y/n) ")
    if ask_answer.lower() == 'y':
        print('Great!')
        start_game = True
    elif ask_answer.lower()=='n':
        print('Maybe another time, then.')
    else:
        ask_answer = ''

if start_game:
    game = Hangman(random.choice(words))
    while game.get_status()=='ongoing':
        print('Remaining wrong guesses: ' + str(game.remaining_guesses) + '\n')        
        print('Current word:', game.get_masked_word())
        next_guess = input('What letter do you guess? ')
        game.guess(next_guess)

    if game.get_status() == 'win':
        print('You Win!')
        print(game.get_masked_word())
    elif game.get_status() == 'lose':
        print('Oh, dear. The word was: ' + game.word)
     