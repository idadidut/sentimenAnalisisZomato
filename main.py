from praprocessing import praprocess

# read file for replacement at pra processing
with open("replacementWord.txt", 'r') as f:
	bar = f.read().split('\n')

word = []
replace = []

for i in bar:
	temp = i.split(" ")
	word.append(temp[0])
	replace.append(temp[1])

with open("reviews.txt", 'r') as f:
	reviews = f.read().split('\n')

words = []
for i in reviews:
	temp = praprocess(i, word, replace)
	words.extend(temp)

f =  open("output.txt", 'w')
for item in words:
	f.write("%s\n" % item)

f.close()