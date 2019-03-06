import re
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_'*len(self.word)

    def guess(self, char):
        char = char.lower()
        word = self.word
        masked_word = self.masked_word
        remaining_guesses = self.remaining_guesses
        
        if self.status != STATUS_ONGOING:
            raise ValueError('Game is over')
        if len(char)>1 or not char.isalpha():
            raise ValueError('Guess must be a single letter')
        
# if the guess is contained and hasn't been made before, update

        if char in word and char not in masked_word:
            matches = re.finditer(char, word)

            for match in matches:
                i=match.start()
                masked_word = masked_word[:i] + char + masked_word[i+1:]
            
            self.masked_word = masked_word
            
            if word==self.masked_word:
                self.status=STATUS_WIN

# if the guess is not contained, reduce remaining guesses and see 
# whether there are any left   
        else:
            remaining_guesses = remaining_guesses - 1
            self.remaining_guesses = remaining_guesses
            if self.remaining_guesses<0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word


    def get_status(self):
        return self.status