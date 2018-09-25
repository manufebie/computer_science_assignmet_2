'''
Exercise 8

Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''

int_list = [22, 55, 10, 17]


def histogram(list):
    print(' HISTOGRAM\n\n')

    # iterate through list and print 
    for i in list:
        print(' * ' * i + '[{}]'.format(i)) # print "*" * i


histogram(int_list)