from collections import Counter

def word_freq(s):
    words = s.split()
    return dict(Counter(words))

def count_words(s):
    print("String: {}".format(s))
    print("Count of words: {}".format(dict(word_freq(s))))

count_words("word") 
count_words("apple and orange and carrot") 



