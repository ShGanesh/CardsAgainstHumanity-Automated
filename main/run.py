#!/usr/bin/python

import random

b = open("blackCards.txt", encoding="utf8")
s = b.read()
l = tuple(s.split("\n"))
b.close()	

r = random.sample(range(len(l)), 10)
ch = int(input("\nInsert Number between 1 and 10: "))
Qu = l[r[ch-1]]

print("\nBlack Card:\n  ", Qu.replace("whitespace", "_________________"))
num = Qu.count("whitespace")

if num == 0 or num == 1:
	n = 1
else:
	n = num

print("\nOpening White Cards...")
w = open("whiteCards.txt", encoding="utf8")
s = w.read()
l = tuple(s.split("\n"))

r = random.sample(range(len(l)), n)
ans = []
for i in r:	
	ans.append(l[i][1:])

for i in ans:
	if num != 0:
		Qu = Qu.replace("whitespace", i, 1)
	else:
		Qu += "\n    "+i
print("  ", Qu)

w.close()


