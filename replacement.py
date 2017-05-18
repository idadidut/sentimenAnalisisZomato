import re

def replaceWord(inputStr, word, replace):
	string = inputStr
	for i in range(len(word)):
		r= re.compile('\s'+word[i]+'\s')
		string = r.sub(' '+replace[i]+' ',string)

	return string