'''
Exercise 9

Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''

def find_longest_word(*args):
    new_string = args.split(',')
    print(new_string)

my_list = ['Superman', 'Batman', 'Wonderman']
find_longest_word(my_list)

