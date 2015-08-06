import re, random
text = file("alice.txt", "r").read()

paragraphs = text.split("\n\n")

tmp = []
for paragraph in paragraphs:
	tmp.append([[re.sub("[^0-9a-zA-Z]", "", y) for y in x.split(" ")] for x in paragraph.split(". ")])

def find_char(c, t):
	if type(t) == str:
		if c in t:
			yield [t.index(c) + 1]
		else:
			yield False
	else:
		for n, a in enumerate(t):
			for x in find_char(c, a):
				if x:
					x.insert(0, n + 1)
					yield x

flag = "allthesechallengenamesaresupercorny"
flag_numbers = []

for c in flag:
	print c
	flag_numbers.append(random.choice([x for x in find_char(c, tmp)]))

with file("lol_numbers.txt", "w") as f:
	for fa in flag_numbers:
		f.write(str(fa) + ", ")