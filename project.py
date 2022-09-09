import random as rd
#import time as time


def lyricsAnalyzer():
    text = """"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    print(text.split())

    word_count = {}
    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)


#lyricsAnalyzer()

def numberGuesser():
    guess = int(input('Welcome to the guessing game. you need to get a number between 1 and 100.')
    #time.sleep(3)
    print('What is your guess? : ')
    correct_no = rd.randint(1,100)
    guess_count = 1

    if guess == correct_no:
        print('Congrats !!!')
    else:
        while guess!= correct_no:
            if guess < correct_no:
                print('Your guess is too small')
            else:
                print('Your guess is too large')
            guess = int(input('What is your guess? : '))

            guess_count += 1

        print(f'Your guess {guess} is correct! It took you {guess_count} tries to get there')
numberGuesser()