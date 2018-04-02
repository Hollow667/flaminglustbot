# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
TWIT_USERNAME = 'bot_lust'

Q_SIZE = 6
HISTORYQ_FILENAME = 'history_q.txt'

TAG_PEN = "sex act with penetration scene"
TAG_NON_PEN = "non-penetrative sex act scene"
TAG_DONE_TO_HER = "done to her scene"
TAG_DONE_TO_HIM = "done to him scene"
TAG_CLIMAX = "orgasm scene"
TAG_POSITION = "sex position scene"
TAG_FOREPLAY = "foreplay scene"
TAG_ABOVE_BELT = "above-the-belt sex act scene"
TAG_BELOW_BELT = "below-the-belt sex act scene"
TAG_ORAL = "oral sex scene"

HistoryQ = None
	
class Gender(Enum):
	Male = 1
	Female = 2
	Neuter = 3
	
class Tense(Enum):
	Present = 1
	Past = 2
	Gerund = 3
	
class LocInOutType(Enum):
	Indoors = 1
	Outdoors = 2
	Either = 3
	
class LocPubPrivType(Enum):
	Public = 1
	Private = 2
	Either = 3
	
class GeneratorType(Enum):
	Normal = 1
	Promo = 2
	Test = 3

def AddArticles(sNounPhrase):
	sUpdatedPhrase = ""
	
	if len(sNounPhrase) > 0:
		if not sNounPhrase[len(sNounPhrase) - 1] == 's':
			if sNounPhrase[0].lower() in ['a','e','i','o','u']:
				sUpdatedPhrase = 'an ' + sNounPhrase
			else:
				sUpdatedPhrase = 'a ' + sNounPhrase
		else:
			sUpdatedPhrase = sNounPhrase
			
	return sUpdatedPhrase

def CoinFlip():
	bHeads = True 
	iRand = randint(1,2)
	if iRand == 2:
		bHeads = False
		
	return bHeads 
	
class WordList:
	List = []
	DefaultWord = ""
	
	def __init__(self, NewList = None):
		if NewList == None:
			pass
		else:
			self.List = NewList
	
	def GetWord(self, sNot = ""):
		sWord = ""
		iRandIndex = 0
			
		if not self.List == None and len(self.List) > 0:
			iRandIndex = randint(0, len(self.List) - 1)
		
			sWord = self.List[iRandIndex]
			while sNot != "" and sNot in sWord:
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
		
class HistoryQ():
	HistoryQ = []
	
	def PushToHistoryQ(self, ID):
		bPushOK = False 
		
		if not self.IsInQ(ID):
			self.HistoryQ.insert(0,ID)
			bPushOK = True
			
			if len(self.HistoryQ) > Q_SIZE:
				self.HistoryQ.pop()
		
		return bPushOK
		
	def IsInQ(self, ID):
		bIsInQ = True 
		
		if not ID in self.HistoryQ:
			bIsInQ = False
		#else:
			#print("Collision: " + str(ID) + " found in Q:")
			#print(self.HistoryQ)
			
		return bIsInQ
			
class HistoryQWithLog(HistoryQ):
	LogFileName = ""
	
	def __init__(self, sLogFileName):
		self.LogFileName = sLogFileName
		#print("LogFileName is " + self.LogFileName)
		
		try:
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		except FileNotFoundError:
			open(self.LogFileName, 'w')
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		#print("Loaded HistoryQ:")
		#print(self.HistoryQ)
			
	def LogHistoryQ(self):
		with open(self.LogFileName, 'w') as WriteHistoryQ:
			for item in self.HistoryQ:
				WriteHistoryQ.write(str(item) + "\n")
		#print("Wrote HistoryQ:")
		#print(self.HistoryQ)
			
