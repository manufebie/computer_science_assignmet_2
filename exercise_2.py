# Exersice 2
# Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.

def calc_length(arg):
    count = 0

    for char in arg:
        count += 1
    
    print('The length of "{}" is: {}'.format(arg, count), end='')
    print()

my_arg = input('Type something and let me calc the length: ')
calc_length(my_arg)