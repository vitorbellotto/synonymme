#!/bin/usr/python
#
# This code has the goal to scrap
# the dictionary website DUDEN for 
# learning purposes using BeautifulSoup
# module.
#
###########################################################

from bs4 import BeautifulSoup
import pickle
import requests
import re

word = 'zart'
meaning = list()

def debugMe( var ):
	print('\n')
	print(var)
	print(type(var))
	print('\n')

def pickleMe( my_dict ):
	pickle_out = open("german_dict.pickle","wb")
	pickle.dump( my_dict, pickle_out )
	pickle_out.close()

def depickleMe( filename ):
	pickle_in = open( filename,"rb")
	return pickle.load(pickle_in)	

def returnStr( bs4object ):
	return "".join([item.encode('utf-8') for item in bs4object.contents])

pattern = re.compile('(.*)<section')

regex = re.compile('span class="lexem"')
url_dic = 'http://www.duden.de/rechtschreibung/' + word

r = requests.get(url_dic)

soup = BeautifulSoup(r.text, 'html.parser')
soup_2 = BeautifulSoup(r.text, 'html.parser')

pattern_a = re.compile('>(.*)<')

i=1
for word_definition in soup.find_all(id='block-duden-tiles-1'):
	for definitions in word_definition.find_all(lambda tag: tag.name == 'ol' and ( tag.get('class') == ['entry'] or tag.get('class') == ['lexem'] ) ):
		for a_link in definitions.find_all(lambda tag: tag.name == 'a'):
			meaning.append("{0} {2}: {1}.".format('Meaning', returnStr(a_link),i))
			print("{0} {2}: {1}.".format('Meaning', returnStr(a_link),i))
			i+=1
	for definitions in word_definition.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lexem']):
			meaning = pattern.search(returnStr(definitions))
			meaning.append("{0} {2}: {1}.".format('Meaning', meaning.group(1),i))
			print("{0} {2}: {1}.".format('Meaning', meaning.group(1),i))
			i+=1

german_dict = { word:meaning }
pickleMe( german_dict )
my_stored_dictionary = depickleMe("german_dict.pickle")
print(my_stored_dictionary)


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


