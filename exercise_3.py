'''
Exercise 3 

Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''

def is_vowel(vowel):
    vowels = ['a', 'e', 'u', 'i', 'o']

    if vowel in vowels:
        print('"{}" is a vowel'.format(vowel))
    else:
        print('"{}" is not a vowel.'.format(vowel))

user_input = input('Type one character: ')
is_vowel(user_input)