#!/bin/usr/python
#
# This class imports search results from
# DUDEN website and stores in a pickle for
# later use.
#
#############################################

import pprint, pickle
from bs4 import BeautifulSoup
import requests
import re


class Dictionary:

	dict_pickle = "german_dict.pickle"
	#meaning = list()

	def __init__(self, word):
		self.word = word
		self.getHTMLaddress()
		
	def getHTMLaddress(self):
		self.url_word = 'http://www.duden.de/rechtschreibung/' + self.word

	def showAttributes(self):
		print('The word is ' + self.word + '.')
		print('The website is ' + self.url_word + '.')

	def getMeaningDict(self):
		self.meaning = self.showDictionary()

	def getMeaningDuden(self):
		meaning = list()
		r = requests.get(self.url_word)

		soup = BeautifulSoup(r.text, 'html.parser')
		soup_2 = BeautifulSoup(r.text, 'html.parser')

		pattern_a = re.compile('>(.*)<')
		pattern = re.compile('(.*)<section')
		regex = re.compile('span class="lexem"')

		i=1
		for word_definition in soup.find_all(id='block-duden-tiles-1'):
			for definitions in word_definition.find_all(lambda tag: tag.name == 'ol' and ( tag.get('class') == ['entry'] or tag.get('class') == ['lexem'] ) ):
				for a_link in definitions.find_all(lambda tag: tag.name == 'a'):
					meaning.append("{0} {2}: {1}.".format('Meaning', self.returnStr(a_link),i))
					i+=1
			for definitions in word_definition.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lexem']):
					meaning = pattern.search(self.returnStr(definitions))
					meaning.append("{0} {2}: {1}.".format('Meaning', meaning.group(1),i))
					print("{0} {2}: {1}.".format('Meaning', meaning.group(1),i))
					i+=1
		self.meaning = meaning

	def getExample(self):	
		pass

	def printMeaning(self):
		for item in self.meaning:
			print(item)

	def getSynonym(self):
		pass

	def getPronunciation(self):
		pass

	def printWord(self):
		pass
		
	def debugMe( var ):
		print('\n')
		print(var)
		print(type(var))
		print('\n')

	def saveWord( self  ):
		pickle_out = open( self.dict_pickle ,"wb")
		pickle.dump( self.meaning, pickle_out )
		pickle_out.close()

	def showDictionary( self ):
		pickle_in = open(self.dict_pickle,"rb")
		de_dict = pickle.load(pickle_in)
		print(type(de_dict))
		return de_dict

	def returnStr( self, bs4object ):
		#for item in bs4object.contents:
		#	expression = "{0}: {1}.".format('Meaning is ', item.encode('utf-8'))
		#	print(expression)
		return "".join([item.encode('utf-8') for item in bs4object.contents])



#german_dict = { word:meaning }
#pickleMe( german_dict )
#my_stored_dictionary = depickleMe("german_dict.pickle")
#print(my_stored_dictionary)


#	print(line)
#	for definition in line.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lexem'],limit=1):
#		print(definition)
#		contents = "".join([str(item) for item in definition.contents])
#		result = pattern.search(contents)
#		print(result.group(1))
#		#result = pattern.search(definition.text)
#		#print(result.group(0))
#	#for definition in line.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lexem'],limit=1):
#	#	print(definition.text + '\n\n\n')

#for child in soup_2.section.descendants:
 #   print(child)
#for link in soup.find_all(lambda tag: tag.name='div' and tag.get('class') == ['entry']):
#	print(link)
#for link in soup.find_all(lambda hat: hat.name='div' and hat.get('class') == ['entry']).find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lexem']):
#    	print(link.text)i

##########################################################################################################################
#
# Essential links used in this code:
# 
#
#


