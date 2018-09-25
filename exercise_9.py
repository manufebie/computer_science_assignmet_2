'''
Exercise 9

Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
'''

words = ['Spiderman', 'Green Goblin', 'Hob Goblin', 'Venom']
length_words = [] # set empty list


def length_of_string(list1, list2):
    # Iterate through list1
    for word in list1:
        length_word = len(word) # use len() method to count length string 
        list2.append(length_word) # append length_word to list2
        print('Length of "{}" is: "{}"'.format(word, length_word)


length_of_string(words, length_words)

