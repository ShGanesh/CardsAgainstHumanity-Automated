#!/usr/bin/python

import sys

f = open(sys.argv[1], "r")
s = f.read()
x = s.replace("\n", " ")
l = x.split(".")

f.close()	
w = open("whiteCards.txt", "w+")
for n in l:
	a = w.write(n)
	a = w.write("\n")
w.close()
