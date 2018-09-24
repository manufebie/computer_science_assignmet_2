'''
Exersice 11

A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: 
"The quick brown fox jumps over the lazy dog". 
Your task here is to write a function to check a sentence to see if it is a pangram or not.
'''

# import string module so it is not neccessary to type the whole alpabet manually
import string

def is_pangram(phrase):
    # set alphabet using the string module
    # both lowercase and uppercase
    alphabet = string.ascii_letters
    print('Phrase is: "{}"'.format(phrase))

    for letter in alphabet: # Iterate through alpabet
        # Checks if phrase contains all letters and displays if so
        if letter in phrase:
            print('Phrase is a pangram')
            break # break so it stops iterating
        else:
            print('Sorry your phrase is not a pangram')
            break
    

my_pangram = 'x' 
is_pangram(my_pangram)