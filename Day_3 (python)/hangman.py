import random
# creating a list of random strings or words
words = ['apple','banana','cherry','kiwi','berry']
# choosing random words by random.choice (python function)
choose_words = random.choice(words)
#create a list of underscore which will essentially look like _ _ _ _ _
words_display = ['_' for _ in choose_words] 
# print(words_display)
# number of attempts user will have
attempts = 8

print("Welcome to Hangman Game!")

# display infinite with will keep running until the user is out of attempts or user guesses wrong.
while attempts > 0 and '_' in words_display:
    # concatenate 
    print("\n" + ' '.join(words_display))
    guess = input("Guess a letter:")
    # determining if the letter guess is present in the list or not
    if guess in choose_words:
        # iterate through each letter of the list
        for index, letter in enumerate(choose_words):
            if letter == guess:
                words_display[index] = guess   #revealing the letter
            else:
                print("letter not in word")
                attempts -=1
# Game conclusion
if '_' not in words_display:
    print("You guessed the word")
    print(' '.join(words_display))
    print("you survived!")
else:
    print("you ran out of attempts. The word was",choose_words)
    print("you lost!")










