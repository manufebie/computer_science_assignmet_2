'''
Exercise 8

Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''
def histogram(*args):

    print(' HISTOGRAM')
    for i in args:
        print(' * ' * i + '[{}]'.format(i))

histogram(1, 22, 55)