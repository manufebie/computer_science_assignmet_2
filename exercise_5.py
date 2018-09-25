'''
Exercise 5:

Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
'''

my_list = [1,2,3,4,5,6,7,8,9,10]


def is_member(x, a):
    for item in a: # Iterates through a (my_list)
        if x == item: # IF x (input) is equal to an item inside a (my_list)
            return '{}: {} is an element of my list'.format(True, x) # return TRUE
    return '{}: {} is not an element of my list'.format(False,x) # Else always return FALSE

# ask user for input
response = int(input('Type a number, and I\'ll tell you if my list contains the element: '))
print(is_member(response, my_list))




