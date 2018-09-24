# Exercise 4
# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse():
    my_string = input('Type something: ')
    reverse = my_string[::-1]
    print('Your input: "{}"'.format(my_string))
    print('Reversed: "{}"'.format(reverse))

reverse()