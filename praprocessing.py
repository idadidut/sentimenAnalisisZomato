from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from replacement import replaceWord
import re


def praprocess(review, word, replace):
	# to lowercase
	reLower = review.lower()

	# remove number and symbol
	r = re.compile('[^a-zA-Z\s]')
	reAlpabetOnly = r.sub(' ',reLower)

	# replace word
	reReplace  = replaceWord(reAlpabetOnly, word, replace)
	r = re.compile('-')
	reReplace = r.sub(' ',reReplace)
	# stemming
	# Stemmer object
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	reStem = stemmer.stem(reReplace)

	result = reStem.split(" ")

	return result