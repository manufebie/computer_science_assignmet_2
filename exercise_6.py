'''
Exercise 6

Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
'''

my_list1 = ['Batman', 'Superman', 'Wonder Woman', 'Martian Manhunter', 'The Flash', 'Captain Marvel']
my_list2 = ['Wolverine', 'Spiderman', 'Daredevil', 'Iron Man', 'Captain Marvel']

def overlapping(x, y):
    # Iterate over list x
    for i in x:
        print('Searching ... ') # print 'Searching ...' just for style
        # Iterate over list y
        for j in y:
            # Compare elements inside list and display element
            # that is inside both list
            if i == j:
                print('\n\n.............')
                print('\n\nMATCH: "{}" is in both lists'.format(i))


overlapping(my_list1, my_list2)