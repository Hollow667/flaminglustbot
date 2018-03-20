# Locations module

import util
import bodyparts

from random import *
from enum import * 

class LocType(Enum):
	Indoors = 1
	Outdoors = 2

class Location():
	Name = ""
	NamePrep = ""
	Loc = LocType.Indoors
	BeginDesc = ""
	EndDesc = ""
	Despite = ""
	BentOver = ""
	KneelingOn = ""
	SittingOn = ""
	HurryReason = ""
	Caught = ""
	Excuse = ""
	Consequence = ""
	Ground = "ground"
	MaleTopClothing = "tshirt"
	MaleBottomClothing = "jeans"
	FemaleTopClothing = "dress"
	FemaleBottomClothing = "panties"
	
	def RemoveMaleClothing(self):
		Penis = bodyparts.Penis()
		sTakeItOff = ""
		
		if not self.MaleTopClothing == "":
			sTakeItOff = "stripped off his " + self.MaleTopClothing + " and pulled down his " + self.MaleBottomClothing 
		else:
			sTakeItOff = "pulled down his " + self.MaleBottomClothing

		sTakeItOff += ", exposing his " + Penis.RandomDescription(bAllowLongDesc = False)	
		
		return sTakeItOff
			
	def RemoveFemaleClothing(self):
		Vagina = bodyparts.Vagina()
		sTakeItOff = ""
		
		if not FemaleTopClothing == "":
			sTakeItOff = "slipped out of her " + self.FemaleTopClothing + " and pulled down her " + self.FemaleBottomClothing
		else:
			sTakeItOff = "pulled down her " + self.FemaleBottomClothing
		sTakeItOff += ", revealing her " + Vagina.RandomDescription(bAllowLongDesc = False)
			
		return sTakeItOff
			
	def PutOnMaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not MaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up"
			else:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up and put on his " + self.MaleTopClothing
		else:
			sPutItOn = "pulled up his " + self.MaleBottomClothing
			
		return sPutItOn
		
	def PutOnFemaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not self.FemaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			else:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing + " and then he helped her into her " + self.FemaleTopClothing
		else:
			sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			
		return sPutItOn
		

class Beach(Location):
	Name = "the beach"
	NamePrep = "at the beach"
	Loc = LocType.Outdoors
	BeginDesc = "A hot sun shone down as blue waves lapped at the sand."
	Despite = "the sand that got into every crack"
	BentOver = "the sand dune"
	KneelingOn = "on the beach towel"
	SittingOn = "on the beach towel"
	HurryReason = "The lifeguard will be here any minute"
	Caught = "'What are you doing?' shouted the lifeguard."
	Excuse = "'We're just putting on lotion!' he replied."
	Consequence = "right in front of the lifeguard"
	Ground = "tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "swim trunks"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "bikini bottoms"
	
class Bedroom(Location):
	Name = "the bedroom"
	NamePrep = "in the bedroom"
	BeginDesc = "The four-poster bed was bathed in warm sunlight as he shut the door behind them."
	Despite = "the open window"
	BentOver = "the king-sized bed"
	KneelingOn = "on the king-sized bed"
	SittingOn = "on the king-sized bed"
	HurryReason = "the neighbors will see us"
	Caught = "'I think the neighbors are watching us!' she said."
	Excuse = "'Let them,' he replied."
	Consequence = "as the neighbors looked on"
	Ground = "thick carpet"
	
class CarBackseat(Location):
	Name = "the backseat of the car"
	NamePrep = "in the backseat of the car"
	BeginDesc = "The couple scrambled into the backseat of the car."
	Despite = "the extremely tight space"
	BentOver = "the back seat"
	KneelingOn = "on the back seat"
	SittingOn = "on the back seat"
	HurryReason = "I hear someone pulling up"
	Caught = "'There was a knock on the steamed-up window. 'Everything OK in there?' asked a cop."
	Excuse = "'Just a little engine trouble,' he replied."
	Consequence = "as the cop shone his flashlight through the window"
	Ground = "leather upholstery"
	
class Church(Location):
	Name = "the church"
	NamePrep = "in the church"
	BeginDesc = "Colored light flooded through a stained glass window."
	Despite = "the sacred atmosphere"
	BentOver = "the pulpit"
	KneelingOn = "on the altar steps"
	SittingOn = "on a pew"
	HurryReason = "someone will catch us in our sin"
	Caught = "'Whis is the meaning of this?' shouted the minister."
	Excuse = "'We were just praying!' he replied."
	Consequence = "as the minister looked on in horror"
	Ground = "soft carpet"
	
#class Gym(Location)
	
class Kitchen(Location):
	Name = "the kitchen"
	NamePrep = "in the kitchen"
	BeginDesc = "S pan of bacon was frying on the kitchen stove."
	Despite = "the crackling of cooking bacon"
	BentOver = "the counter"
	KneelingOn = "on a kitchen chair"
	SittingOn = "on the kitchen table"
	HurryReason = "the bacon will burn"
	Caught = "The pan of bacon began to smoke."
	Excuse = "'We'll just make some more!', he said."
	Consequence = "as the fire alarm blared"
	Ground = "black and white tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "briefs"
	FemaleTopClothing = "oversized tshirt"
	FemaleBottomClothing = "panties"
	
class Library(Location):
	Name = "the library"
	NamePrep = "in the library"
	BeginDesc = "It was quiet and stuffy amongst the stacks."
	Despite = "the need for silence"
	BentOver = "a stack of books"
	KneelingOn = "on a table strewn with books"
	SittingOn = "on a study desk"
	HurryReason = "someone will hear us"
	Caught = "'Please, you must be quiet!' called out a librarian."
	Consequence = "as the librarian listened"
	Excuse = "'We are just about to check out!' he called back."
	Ground = "soft carpet"
	FemaleBottomClothing = "thong"
	
class MensRoom(Location):
	Name = "men's restroom"
	NamePrep = "in the men's restroom"
	BeginDesc = "Crude graffiti was scrawled on the walls of the cramped stall."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Consequence = "as someone called out 'Fuck her good, man'"
	Excuse = "'Busy!' he shouted back."
	Ground = "tiled floor"
	FemaleBottomClothing = "thong"
	
#class Office(Location)
#pass
	
class StarbucksBathroom(Location):
	Name = "Starbucks bathroom"
	NamePrep = "in the bathroom at Starbucks"
	BeginDesc = "The bathroom at Starbucks was small and smelled of coffee."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Excuse = "'Busy!' he shouted back."
	Consequence = "as someone called, 'I think they're having sex in the Starbucks bathroom'"
	Ground = "tiled floor"
	
class Surf(Location):
	Name = "the surf"
	NamePrep = "in the water at the beach"
	Loc = LocType.Outdoors
	BeginDesc = "A hot sun shone down as the waves crested against their bodies."
	Despite = "the breaking waves"
	BentOver = "in the water"
	KneelingOn = "in the shallow water"
	SittingOn = "in the shallow water"
	HurryReason = "People will notice us!"
	Caught = "'That lifeguard is coming towards us!' she said."
	Excuse = "'Let them enjoy it, baby,' he said."
	Consequence = "as the lifeguard watched"
	Ground = "the dark green water"
	MaleTopClothing = ""
	MaleBottomClothing = "speedos"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "g-string"
	
class Woods(Location):
	Name = "the woods"
	NamePrep = "out in the woods"
	Loc = LocType.Outdoors
	BeginDesc = "The leafy trees were thick in every direction."
	Despite = "the dirt and mosquitos"
	BentOver = "a mossy log"
	KneelingOn = "a large smooth rock"
	SittingOn = "a tree stump"
	HurryReason = "someone might see us"
	Caught = "'Oh my god, there is a homeless guy watching us,' she whispered."
	Excuse = "'Fuck off!' he yelled at the man."
	Consequence = "as the homeless man watched them"
	Ground = "thick carpet of leaves"
	FemaleBottomClothing = "thong"
	
#class YogaStudio(Location):
# seated on a yoga ball
	

	
class LocationSelector():
	Locations = []
	
	def __init__(self):
		for sub in Location.__subclasses__():
			self.Locations.append(sub())
	
	def Location(self):
		iRand = randint(0, len(self.Locations) - 1)
		
		return self.Locations[iRand]
	
	