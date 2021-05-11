#Ex 25  ---- Even more practice

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort th words"""
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print (word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words"""
    words = break_words(sentence)
    return (sort_words(words))

def print_first_and_last(sentence):
    """print first and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = break_words(sentence)
    s_words = sorted(words) #or sort_words
    print_first_word(s_words)
    print_last_word(s_words)

