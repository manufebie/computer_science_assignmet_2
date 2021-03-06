'''
Exercise 9

Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''

def find_longest_word(my_list):
    # using max method to find longest string inside using len for key
    # and us len method to print out the length of the longest string
    print('Longest string length is: {}'.format(len(max(my_list, key=len))))
        
heroes = ['Superman', 'Batman', 'Wonder Woman', 'Martian Manhunter']
find_longest_word(heroes)