def count_words (text):
    words = text.split( )
    return len(words)

example_text = ('hi im luka and im making exaple of count words')
word_count = count_words(example_text)
print (word_count)