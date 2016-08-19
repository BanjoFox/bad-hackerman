#!/usr/bin/python

import random

colorList = ["Blue", "Green", "Red", "Yellow"]
randColor = random.choice(colorList)

def roomContents():
	# Each room can have one of:
	# 1. An ADV
	# 2. An access card
	# 3. A Probe (more on this in a little bit)
	# 4. A hazard
	# 5. The virus (presumably chilling out)
	# 6. Nothing at all
	
	advList = ["Decoder", "Disruptor", "Negatron"]
	randADV = random.choice(advList)

	accessCardList = randColor + " Access Card"

	probeList = randColor + " Probe"

	hazardList = ["BOOM!", "POW!", "BIFF!", "SHAZAM!"]
	randHazard = random.choice(hazardList)

	contents = [randADV, accessCardList, probeList, randHazard, "Virus", "Nothing"]
	return random.choice(contents)

class room:
    def __init__(self, sector, number, color, contents):
        self.sector = sector
        self.number = number
        self.color = color
        self.contents = roomContents()
	
    def displayRoom(self):
	print "Room Sector: ", self.sector,  ", Number: ", self.number, ", Color: ", self.color, ", Contents: ", self.contents


#def items():
	# Four of each, to be distributed across the map.
	# Access keys (Blue, Red, Yellow)
	# Decoder - yellow
	# Disruptor - blue
	# Negatron - red
	# Probe

# Sample room definitions
r000 = room("red", "000", "blue", "")
r100 = room("yellow", "100", "green", "")

r000.displayRoom()
r100.displayRoom()

