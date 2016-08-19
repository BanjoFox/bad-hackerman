#!/usr/bin/python

import random


class room:
    def __init__(self, sector, number, color, contents):
        self.sector = sector
        self.number = number
        self.color = color
        self.contents = contents
	
    def displayRoom(self):
	print "Room Sector: ", self.sector,  ", Number: ", self.number, ", Color: ", self.color, ", Contents: ", self.contents
	
firstRoom = room("red", "000", "blue", "nothing")
secondRoom = room("yellow", "100", "green", "greenProbe")


firstRoom.displayRoom()
print secondRoom.contents

'''		
blueRooms = ("000", "001");
greenRooms = ("010", "100"); 
redRooms = ("101","110");
yellowRooms = ("111", "200"); 

roomList = blueRooms + greenRooms + redRooms + yellowRooms

print "Blue: ", blueRooms
print "Green: ", greenRooms
print "All :", roomList

'''

