#!/usr/bin/python

import random

# Greetings
greetings = '''
		CardsAgainstHumanity-Automated (basic)
 An Automated (and slightly modified) version of Cards Against Humanity.

 In this game, players complete fill-in-the-blank statements using words or phrases typically deemed risque. 
 
 Text file blackCards.txt contains questions which initiate an instance of a CAH game.
 Text file whiteCards.txt contains ... weird phrases which can be added to questions from the blackCards.txt
 
 
 To Start the Game, the Card Czar shall draw one card out of the 10 randomized black cards provided by the script.
 The script shall randomly select phrases from whiteCards.txt and attach them to the provided Question. The Card Czar has to read the output statement out loud. 
 The person who loses their sh*t first shall become the new Card Czar and continue the cycle.
 If the current Card Czar fails to make anyone laugh they shall start acting like a sentient monkey and then initiate another instance of the game.
 Additional failiures shall lead to the Card Czar accepting different genera, which shall be left to the descretion of other players.

'''


def inp(): # If 'y' save input in file. Else, don't. If invalid input repeat function.
	sss = input(" Do you want to save outputs in another file? (y/n):\t")
	if sss == 'Y' or sss == 'y':
		print("Output will be appended to file named 'CAH_OP.txt'.")
		return True
	elif sss == 'N' or sss == 'n':
		print("Output will not be saved.")
		return False
	else:
		print(" Please clarify... (y/n).")
		return inp()


def black(j, ch): 	# Select and print BlackCard Statement. Returns BlackCard statement and number of whitespaces.
	b = open("blackCards.txt", encoding="utf8")
	s = b.read()
	l = tuple(s.split("\n"))	# Tuple having all questions from list of black cards
	b.close()
	
	# Randomization NOW
	r = tuple(set(random.sample(range(len(l)-1), 10)))
	print("\n\t__START_GAME__", i)
	Qu = l[r[ch-1]] 	# index(index (ch) in tuple r) in list of black cards
	
	print(" \tYour Black Card:\n \t  ", Qu.replace("whitespace", "_________________"))
	num = Qu.count("whitespace")
	if num == 0:
		num = 1
	return Qu, num


def white(Qu, num): 	# Get whiteCard phrases and attach them to BlackCard statements.
	print("\n\t Opening White Card(s)...")
	w = open("whiteCards.txt", encoding="utf8")
	s = w.read()
	l = tuple(s.split("\n"))
	w.close()	
	r = tuple(set(random.sample(range(len(l)-1), num)))
	
	ans = []
	for i in r:	
		ans.append(l[i][1:])
	
	for i in ans:
		if Qu.count("whitespace") != 0:
			Qu = Qu.replace("whitespace", i, 1)	# replaces each whitespace with random phrases one-by-one
		else:
			Qu += "\n\t   "+i
	
	print("\t WhiteCard(s) = ")
	print("\t\t ", ', '.join(ans))

	return Qu
	

# Main Function
print(greetings)
#print("\n")
i = 0
x = inp()						# Only asks once... If you wanna save outputs or not.
while True:
	ch = input("\n Choose your BlackCard!\n \tInsert Number between 1 and 10 (type exit to exit): ")	# Choose one from 10 random black cards
	if ch == "exit":
		print("\n Thenks for playing this game for", i, "iteration(s)")
		break
	else:
		i += 1
		a = tuple(black(i, int(ch)))
		res = white(a[0], a[1])
		print("-"*len(res)*int(3/2))
		print(" ", res)
		print("-"*len(res))
	
		if x:
			a = open("CAH_OP.txt", "a")		# Appends into file. If file doesn't exist, it creates one.
			a.write("\n")
			a.write(res)
			a.write("\n")
			a.close()

