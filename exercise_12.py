'''
Exersice 12

In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:
a) If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
b) If the verb ends in ie, change ie to y and add ing
c) For words consisting of consonant-vowel-consonant, double the final letter before adding ing
d) By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
'''

# if verb end in e, slice e and add ing
# if verb ends in ie, change ie to y and add ing
# be default add 'ing' to end of string

def make_ing_form(verb):
    extension1 = 'ying'
    extension2 = 'ing'
    exceptions = ['be', 'see', 'flee', 'knee']
    split_verb = list(verb)

    # words ending with 'ie' into 'ying'
    if verb.endswith('ie'):
        # delete last 2 chars (ie)
        del split_verb[-2:] # delete last 2 chars from list
        split_verb.append(extension1) # append new form
        present_verb = ''.join(split_verb) # set present_verb to string form of split_verb
        return present_verb
    elif verb.endswith('e'):
        del split_verb[-1:]
        split_verb.append(extension2)
        present_verb = ''.join(split_verb) 
        return present_verb
    
print(make_ing_form('be'))
print(make_ing_form('See'))
print(make_ing_form('die'))
print(make_ing_form('lie'))