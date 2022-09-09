
my_list = [1,2,3,4,5,6,7]
print(my_list)

new_list = [2 * item for item in my_list]
print(new_list)

another_list = [item for item in new_list if item % 4 == 0]
print(another_list)

def cleanWord(word):
    return word.replace('.','').lower()

my_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

clean_word = [cleanWord(word) for word in my_string.split() if len(word) < 3]
print(clean_word)

# nested list Comprehension

nested = [[cleanWord(word) for word in sentence.split()] for sentence in my_string.split('.')]
print(nested)
