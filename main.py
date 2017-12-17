#!/bin/usr/python
#
# This code has the goal to scrap
# the dictionary website DUDEN for 
# learning purposes using BeautifulSoup
# module.
#
###########################################################

from Dictionary import *
from Book import *

my_word = 15
book = Book('book.txt')
simplelist = [Dictionary(word) for word in book.highlighted_words]
print(simplelist[my_word].url_word)
simplelist[my_word].getMeaningDuden()
simplelist[my_word].printMeaning()

#for word_dict in simplelist:
#	word_dict.getMeaningDuden()
#	word_dict.saveWord()


one_word = Dictionary('zart')
one_word.getMeaningDict()
#one_word.saveWord()
one_word.printMeaning()
