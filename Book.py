#!/usr/bin/python
#
# The goal of this code is to read all words from the exported files 
# of my tablet app. The file is exported in txt format.
#
################################
#
# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
#
#
################################################################

import re
import os.path
from pprint import pprint

class Book:

	def __init__(self, book_file):
		if os.path.isfile(book_file):
			self.getHighlightedWords( book_file )

	def getHighlightedWords( self, book_file ):
		content_regex = re.compile('"(\w*)"',re.UNICODE)
		file_object = open( book_file,'r')
		self.highlighted_words = content_regex.findall(file_object.read())

	def printList( self ):
		try:
			pprint(self.highlighted_words)
		except AttributeError:
			print('No list of highlighted words has been found.')		
