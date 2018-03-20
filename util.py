# Utilities module

import time, sys, random

from random import *
from enum import * 

def AddArticles(sNounPhrase):
	sUpdatedPhrase = ""
	
	if not sNounPhrase[len(sNounPhrase) - 1] == 's':
		if sNounPhrase[0].lower() in ['a','e','i','o','u']:
			sUpdatedPhrase = 'an ' + sNounPhrase
		else:
			sUpdatedPhrase = 'a ' + sNounPhrase
	else:
		sUpdatedPhrase = sNounPhrase
		
	return sUpdatedPhrase
	
class Gender(Enum):
	Male = 1
	Female = 2
	Neuter = 3
	
class WordList:
	List = []
	DefaultWord = ""
	
	def __init__(self, NewList = None):
		if NewList == None:
			pass
		else:
			self.List = NewList
	
	def GetWord(self):
		sWord = ""
		iRandIndex = 0
			
		if not self.List == None and len(self.List) > 0:
			iRandIndex = randint(0, len(self.List) - 1)
		
			sWord = self.List[iRandIndex]
		
		return sWord
		
class NounAdjList:
	NounList = []
	AdjList = []
	DefaultNoun = ""
	DefaultAdj = ""
	
	def __init__(self, NewNounList = None, NewAdjList = None):
		if NewNounList == None:
			pass
		else:
			self.NounList = NewNounList
			
		if NewAdjList == None:
			pass
		else:
			self.AdjList = NewAdjList
	
	def GetNoun(self):
		sNoun = ""
		
		iRandNounIndex = 0
		
		if not self.NounList == None and len(self.NounList) > 0:
			iRandNounIndex = randint(0, len(self.NounList) - 1)
			
		sNoun = self.NounList[iRandNounIndex]
		
	def GetAdj(self):
		sAdj = ""
		
		iRandAdjIndex = 0
		
		if not self.AdjList == None and len(self.AdjList) > 0:
			iRandAdjIndex = randint(0, len(self.AdjList) - 1)
			
		sNoun = self.AdjList[iRandAdjIndex]
	
	def GetWord(self):
		sWord = ""
					
		sWord = self.GetAdj() + " " + self.GetNoun()
		
		return sWord