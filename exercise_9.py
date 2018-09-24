'''
Exercise 9

Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
'''

words = ['Spiderman', 'Green Goblin', 'Hob Goblin', 'Venom']
length_words = []

def length_of_string(list1, list2):
    # Iterate through list of strings
    for word in list1:
        length_word = len(word)
        list2.append(length_word)
        print('Length of "{}" is: "{}"'.format(word, length_word)
    
length_of_string(words, length_words)

