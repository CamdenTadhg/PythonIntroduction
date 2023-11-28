def print_upper_words(words):
    '''for a list of words, prints each word on a separate line in all upper case'''
    for word in words:
        print(word.upper())

def print_upper_e_words(words):
    '''for a list of words, prints each word that starts with an e in all upper case'''
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())


def print_upper_limited_words(words, must_start_with):
    '''given a list of words and a list of letters, print each word that starts with one of those letters in upper case'''
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter):
                print(word.upper())

print_upper_limited_words(["Hello", "hey", "goodbye", "Yo", "yes"], must_start_with={"h", "y"})