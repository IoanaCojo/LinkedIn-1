import random as rd

animalList = [('a','aligator'),('b','bear'), ('c','cat'),('d','dog')]
animals = {item[0]: item[1] for item in animalList}
print(animals)

animals2 = {key:value for key,value in animalList}
print(animals2)

#turning it back into a list
print(list(animals.items()))

#return a list of dictionary2 items
lst = [{'letter':key, 'name': value} for key, value in animals.items()]
print(lst)