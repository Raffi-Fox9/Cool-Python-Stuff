class Deck:
	from random import shuffle as shuffler
	__suits = ['Spades','Hearts','Clubs','Diamonds']
	__values = [str(x) for x in range(2,11)] + ['Jack','Queen','King','Ace']

	def __init__(self,value=1):
		self.__cards = self.__setCards()*value
		self.__index = -1
		self.__shuffled = False

	def __str__(self):
		return "There are %d cards in this deck." %(len(self.__cards))

	def __iter__(self):
		return self
	
	def __next__(self):
		self.__index += 1
		if self.__index == len(self.__cards):
			self.__index = -1
			raise StopIteration
		else:
			return self.__cards[self.__index]
		#end if   

	def __setCards(self):
		return [Card(suit,value) for suit in self.__suits for value in self.__values]
	
	def shuffle(self):
		return self.shuffler(self.__cards)
	
	def getDeck(self):
		return self.__cards
#end Deck 

class Card:
	def __init__(self,suit,value):
		self.__suit = suit
		self.__value = value
	
	def __str__(self):
		return "%s of %s" %(self.getValue(),self.getSuit())

	def getValue(self):
		return self.__value
	
	def getSuit(self):
		return self.__suit
#end Card

def val(word):
	'''returns the value of a card (and converts face cards to numerical values)
	--param
	word:str
	--return
	str
	'''
	if word == 'Jack':
		word = '11'
	elif word == 'Queen':
		word = '12'
	elif word == 'King':
		word = '13'
	elif word == 'Ace':
		word = '14'
	return word
	#end if   
#end fTN
def war(h1,h2):
	'''war plays out the 'war' scenario
	--param
	h1:list
	h2:list
	--return
	str
	'''
	#input("Press any key to continue: ")
	won = ''
	pos = 0
	count = 0
	while won == '':
		print("WAR!!!!!")
		count += 1
		pos += 3
		if len(h1) < 5:
			card1 = h1[-1]
		else:
			card1 = h1[pos]
		#end if
		if len(h2) < 5:
			card2 = h2[-1]
		else:
			card2 = h2[pos]
		#end if
		print("Player one's war card: ",card1)
		print("Player two's war card: ",card2)
		#input("Press enter to play: ")
		card1 = int(val(card1.getValue()))
		card2 = int(val(card2.getValue()))
		if card1 > card2:
			won = 'Player 1'
			return won,count
		elif card2 > card1:
			won = 'Player 2'
			return won,count
		else:
			pass
		#end if 
	#end while
#end war

print("Welcome to the card game of War!")
input("Press enter to play: ")

deck = Deck()
deck.shuffle()
deckList = []
for i in deck:
	deckList.append(i)
#end for
p1h = deckList[0:26]
p2h = deckList[26:]

while len(p1h) != 0 and len(p2h) != 0:
	p1c = p1h[0]
	p2c = p2h[0]
	print("Player one's card: ",p1c)
	print("Player two's card: ",p2c)

	#input("Press any key to continue: ")

	p1c = int(val(p1c.getValue()))
	p2c = int(val(p2c.getValue()))

	if p1c > p2c:
		p1h.append(p2h[0])
		p2h.remove(p2h[0])
		p1h.append(p1h[0])
		p1h.remove(p1h[0])
	elif val(p2c) > val(p1c):
		p2h.append(p1h[0])
		p1h.remove(p1h[0])
		p2h.append(p2h[0])
		p2h.remove(p2h[0])
	else: #war
		winner = war(p1h,p2h)
		if winner[0] == 'Player 1':
			for i in range(1,winner[1]+1):
				p1h += p2h[0:6]	
				#end for
				p2h = p2h[6:]
				p1h.append(p1h[0])
				p1h.remove(p1h[0])
			#end for 
		else:
			for i in range(1,winner[1]+1):
				p2h += p1h[0:6]	
				p1h = p1h[6:]
				p2h.append(p2h[0])
				p2h.remove(p2h[0])
			#end for 
		#end if	
	#end if    
	print("Player one has %d cards left" %len(p1h))
	print("Player two has %d cards left" %len(p2h))
#end while
if len(p1h) == 0:
	print("Player two wins!")
else:
	print("Player one wins!")
