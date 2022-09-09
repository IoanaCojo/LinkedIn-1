import random as rd

#print(rd.randint(1,10))
#print(rd.random())


def magic8():
    answer = rd.randint(1,3)

    if answer == 1:
        print('Yes')
    elif answer == 2:
        print('Maybe')
    else:
        print('No')


def luckyNumber():
    lucky_no = rd.randint(1,100)
    fortune_no = rd.randint(1,3)
    fortune_text = ''

    if fortune_no == 1:
        fortune_text = 'You will have a great day'
    elif fortune_no == 2:
        fortune_text = 'Today will be tough, but stick to it'
    else:
        fortune_text =' Not so lucky !'

    print(f'{fortune_text}. Your lucky number is {lucky_no}')


def listPractice():
    fav_movies = ['movei1', 'movie2', 'movie3']
    print(f'My fav, fav movie is {fav_movies[2]}')
    print(f'I have {len(fav_movies)} fav movies')
    fav_movies.append('Iron Man')
    print(f'My fav, fav movie is {fav_movies[3]}')
    print(f'I have {len(fav_movies)} fav movies')

    # put an item in a specific place
    fav_movies.insert(1,'Batman')
    print(f'Adding an el to a specific location 1 - batman : {fav_movies}')

    # delete an item
    del(fav_movies[3])
    print(f'Del an element {fav_movies}')


def forLoops():
    for number in range(2, 10):
        print(number)

    fav_movies = ['movie1', 'movie2', 'movie3']
    for movie in fav_movies:
        print(movie)


def dictPractice():
    cats = {
        'Jane': [6,9],
        'Tom': 14,
        'Sarah': 8
    }

    '''    
    print(cats)
    print(cats['Tom'])
    cats['Wilson'] = 1
    del(cats['Tom'])
    print(cats)
    '''
    print(cats.keys())
    key = list(cats.keys())
    val = cats.values()

    #print(val)

    el = cats.get('tom', 'element not in the list ')
    print(el)

    print(len(cats))

    cats['Jane'].append(6)
    print(cats)


def userInput():
    user_text = input('Enter some Text: ')
    print(user_text.upper())

    user_no = input('Enter a number: ')
    print(int(user_no)*2)

def upperOrLower():
    user_text = input('Enter your string here :  ')
    choice = input('if you want it upper pres 1 else press 2: ')

    '''    
    if choice != '1' or choice!='2':
    while choice != '1' or choice != '2':
    choice = input('Please enter 1 or 2 : ')
    '''
    if int(choice) == 1:
        print(user_text.upper())
    elif choice == '2':
        print(user_text.lower())


'''
print('Result for magic8 function :')
magic8()
print('\n')

print('Result for luckyNumber function :')
luckyNumber()
print('\n')

print('Result for listPractice function :')
listPractice()
print('\n')


print('Result for forLoops() function :')
forLoops()
print('\n')

print('Result for dict function :')
dictPractice()
print('\n')

print('Result for userInput function :')
userInput()


upperOrLower()
'''
