# Misc module

import people
import verbs
from random import *
from util import *
		
class Events(WordList):
	List = ['Ash Wednesday',
		'Christmas Eve',
		'Easter Sunday',
		'Halloween',
		'Highschool Graduation',
		'Homecoming',
		'Independence Day',
		'International Women\'s Day',
		'Junior Prom',
		'Mardis Gras',
		'Mother\'s Day',
		'my anniversary',
		'my birthday',
		'my wedding day',
		'New Year\'s Eve',
		'Spring Break',
		'St. Patrick\'s Day',
		'Superbowl Sunday',
		'teacher planning day',
		'Valentine\'s Day']
		
	def RemoveMy(self, sWord):
		return sWord.replace('my ','')
		
	def GetWord(self, bRemoveMy = False):
		sEvent = ""
		
		sEvent = super().GetWord()
			
		if bRemoveMy:
			sEvent = self.RemoveMy(sEvent)
			
		return sEvent
		
class Hashtags(WordList):
	List = ['amwriting',
			'BDSM',
			'bitcoin',
			'blockchain',
			'bot',
			'botlife',
			'botlove',
			'eartg',
			'eartg',
			'erotica',
			'erotica',
			'fantasy',
			'fiftyshades',
			'filthy',
			'lprtg',
			'lprtg',
			'mrbtg',
			'naughty',
			'nsfw',
			'PleaseRT',
			'romance',
			'smut',
			'sorrynotsorry',
			'ssrtg',
			'ssrtg',
			'taboo',
			'truelove',
			'twitterbot',
			'twitterbot']
		
class BadGirlNames(WordList):
	List = ['hussy',
		'minx',
		'nympho',
		'skank',
		'slut',
		'slut',
		'slut',
		'tart',
		'tramp',
		'trollop',
		'whore',
		'whore']
		
	AdjList = ['brazen',
		'cheeky',
		'filthy',
		'little',
		'nasty',
		'outrageous',
		'saucy',
		'shameless',
		'wanton']
		
	def GetAdj(self):
		sAdj = ""
		
		if len(self.AdjList) > 0:
			iRand = randint(0, len(self.AdjList) - 1)
			
			sAdj = self.AdjList[iRand]
		
		return sAdj
		
class Exclamations(WordList):
	List = ['baby',
		'damn',
		'fuck',
		'fuck',
		'fuck',
		'fuck',
		'fuck me',
		'fuck me',
		'hell',
		'holy shit',
		'God',
		'God',
		'god damn',
		'gosh',
		'jeez',
		'Jiminy Christmas',
		'holy motherfucking shit',
		'lord',
		'oh goodness',
		'oh my',
		'shit',
		'shit',
		'sweet Mother Mary',
		'tits']
		
	def GetWord(self, bHappy = False, bSad = False, bExMk = True):
		sExclamation = ""
		iRand = 1
		
		sExclamation = super().GetWord()
		
		iRand = randint(1, 3)
		if iRand == 1 and not "oh " in sExclamation:
			sExclamation = "oh " + sExclamation
			
		iRand = randint(1, 3)
		if iRand == 1 and bHappy:
			if CoinFlip():
				sExclamation += ", yes"
			else:
				sExclamation += ", yeah"
		elif iRand == 1 and bSad:
			sExclamation += ", no"
			
		if bExMk:
			sExclamation += "!"
			
		return sExclamation
		
class TermsOfEndearment(WordList):
	List = ['babe',
		'baby',
		'darling',
		'dear',
		'honey',
		'love',
		'my love',
		'sweetie',
		'sweetheart']
		
class SexyAdjs(WordList):
	List = ['dirty',
		'filthy',
		'hot',
		'naughty',
		'sexy',
		'steamy']
		
class WomanAdjs(WordList):
	def __init__(self):
		self.List = ['beautiful',
			'busty',
			'buxom',
			'comely',
			'curvaceous',
			'curvy',
			'elegant',
			'gorgeous',
			'leggy',
			'lewd',
			'model-esque',
			'MILF-esque',
			'nubile',
			'petite',
			'ravishing',
			'saucy',
			'sensual',
			'sexy',
			'shameless',
			'shapely',
			'slender',
			'statuesque',
			'stunning',
			'sultry',
			'teenage',
			'voluptuous',
			'young',
			'youthful']

class BookSellers(WordList):
	List = ['Apple Books',
			'Amazon',
			'B&N',
			'Kobo',
			'Radish Fiction',
			'Smashwords',
			'WattPad']
			
class BookGirls(WordList):
	List = ['Amish Maiden',
			'Babysitter',
			'BBW',
			'Call-Girl',
			'Co-ed',
			'Concubine',
			'Fashion Model',
			'Flight Attendant',
			'Futa',
			'Governess',
			'Handmaiden',
			'Harem Girl',
			'Hotwife',
			'Housewife',
			'French Maid',
			'Librarian',
			'Maiden',
			'Masseuse',
			'Midwife',
			'MILF',
			'Milk Maid',
			'Nanny',
			'Nurse',
			'Surrogate',
			'Secretary',
			'Servant',
			'Sex Slave',
			'Sex Witch',
			'Single Mom',
			'Small-Town Girl',
			'Step-Daughter',
			'Step-Sister',
			'Submissive',
			'Teacher',
			'Tutor',
			'Virgin',
			'Waitress',
			'Wife']
			
class BookGirlAdjs(WordList):
	List = ['Amish',
		'BBW',
		'BDSM',
		'Call-Girl',
		'Co-ed',
		'Concubine',
		'Curvy',
		'Fertile',
		'Futa',
		'Harem',
		'Hotwife',
		'High-Heeled',
		'Innocent',
		'Intern',
		'Lesbian',
		'Married',
		'MILF',
		'Naked',
		'Pregnant',
		'Sex',
		'Single',
		'Single Mom',
		'Small-Town',
		'Submissive',
		'Taboo',
		'Teenage',
		'Virgin',
		'Virgin',
		'Virgin',
		'Virgin']

class BookMasters(WordList):
	List = ['Alpha',
			'Alpha Wolf',
			'Assassin',
			'Baby Daddies',
			'Barbarian',
			'Barbarians',
			'BBC',
			'Biker',
			'Biker Gang',
			'Billionaire',
			'Bitcoin Billionaire',
			'Boss',
			'Breeding Stud',
			'CEO',
			'Count',
			'Cop',
			'Cowboy',
			'Cowboys',
			'Dad',
			'Daddy Dom',
			'Dildo Designer',
			'Dinosaur',
			'Doctor',
			'Dom',
			'Dominatrix',
			'Duke',
			'Futanari',
			'Gazillionaire',
			'Goat Man',
			'Goat Men',
			'Hitman',
			'Fire Fighter',
			'King',
			'Knight',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lesbian Harem',
			'Lesbian MILF',
			'Lipstick Lesbian',
			'Older Man',
			'Male Escort',
			'Male Stripper',
			'Man-o-taur',
			'Manor Lord',
			'Man-telope',
			'Man-ticore',
			'Marquis',
			'Mer-man',
			'MMA Fighter',
			'Millionaire',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Navy Seals',
			'Pirate Captain',
			'Pirates',
			'Playboy Billionaire',
			'Pope',
			'President',
			'Prince',
			'Professor',
			'Rock Star',
			'Shah',
			'Sex Warlock',
			'Sheikh',
			'Sheriff',
			'Surfer',
			'Trillionaire',
			'Viking',
			'Viking Hoard',
			'Uniporn',
			'Vampire',
			'Vampire Coven',
			'Werewolf',
			'Werewolf Pack']
			
class BookMasterAdjs(WordList):
	List = ['Alpha',
			'Bad Boy',
			'Bitcoin Billionaire',
			'Biker',
			'Billionaire',
			'Black',
			'Cowboy',
			'Dinosaur',
			'Fire Fighter',
			'French',
			'Futanari',
			'Gazillionaire',
			'Goat Man',
			'Highlander',
			'Hitman',
			'Horny',
			'Irish',
			'Italian',
			'Mer-man',
			'Millionaire',
			'MMA Fighter',
			'Mountain Man',
			'Multi-Millionaire',
			'Naked',
			'Navy Seal',
			'Older Man',
			'Pirate',
			'Playboy',
			'Rock Star',
			'Savage',
			'Scottish',
			'Secret',
			'Secret',
			'Shape-Shifting',
			'Single Dad',
			'Space',
			'Spanish',
			'Stay-at-Home',
			'Stripper',
			'Surfer',
			'Trillionaire',
			'Viking',
			'Well-hung',
			'Werewolf']
			
class BookVerbsBy(WordList):
	List = ['Blackmailed',
			'Bound',
			'Bred',
			'Claimed',
			'Claimed in Public',
			'Conquered',
			'Charmed',
			'Cuckolded',
			'Dominated',
			'Enslaved',
			'Exposed in Public',
			'Forced',
			'Hotwifed',
			'Humiliated',
			'Hunted For Food',
			'Impregnated',
			'Knocked Up',
			'Mastered',
			'Owned',
			'Pleasured',
			'Punished',
			'Punished in Public',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Spanked',
			'Spanked in Public',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Taken',
			'Taken in Public',
			'Tempted',
			'Trained',
			'Secretly Watched']
			
class BookVerbsTo(WordList):
	List = ['Bred',
			'Bound',
			'Cuckquean',
			'Engaged',
			'Enslaved',
			'Hotwife',
			'Hotwifed',
			'Lolita',
			'Married',
			'Mated',
			'Sold',
			'Submissive',
			'Submitting']
			
class BookTitleBuilder():
	def GetMaster(self):
		sMaster = ""
		
		Masters = BookMasters()
		MasterAdjs = BookMasterAdjs()
		
		iRand = randint(1,2)
		sMaster = Masters.GetWord()
		sMasterAdj = MasterAdjs.GetWord()
		if iRand == 2:
			while sMasterAdj in sMaster:
				sMasterAdj = MasterAdjs.GetWord()
			sMaster = sMasterAdj + " " + sMaster
			
		return sMaster
		
	def GetGirl(self):
		sGirl = ""
		
		Girls = BookGirls()
		GirlAdjs = BookGirlAdjs()
		
		iRand = randint(1,7)
		sGirl = Girls.GetWord()
		sGirlAdj = GirlAdjs.GetWord()
		if iRand > 3 and iRand < 7:
			while sGirlAdj in sGirl:
				sGirlAdj = GirlAdjs.GetWord() 
			sGirl = sGirlAdj + " " + sGirl
		elif iRand == 7:
			while sGirlAdj in sGirl:
				sGirlAdj = GirlAdjs.GetWord()
			sGirl = sGirlAdj + " " + sGirl
			
			sGirlAdj = GirlAdjs.GetWord()
			while sGirlAdj in sGirl:
				sGirlAdj = GirlAdjs.GetWord()
			sGirl = sGirlAdj + " " + sGirl
			
		return sGirl
		
	def _getFMs_(self):
		FMs = ""
		
		iRandLen = randint(4,10)
		for x in range(1, iRandLen):
			iRandChoice = randint(1,3)
			if iRandChoice == 1:
				FMs += "F"
			else:
				FMs += "M"
				
		if "M" not in FMs:
			FMs += "M"
		elif "F" not in FMs:
			FMs += "F"
		
		return FMs
		
	def GetTitle(self):
		sTitle = ""
		
		Masters = BookMasters()
		VerbsBy = BookVerbsBy()
		VerbsTo = BookVerbsTo()
		
		sGirl = self.GetGirl()
		sMaster = self.GetMaster()
		sVerbBy = VerbsBy.GetWord()
		sVerbTo = VerbsTo.GetWord()
		
		iRand = randint(1,15)
		if iRand == 1:
			#Blackmailed by the Billionaire Mountain Man 
			sTitle = sVerbBy + " by the " + sMaster
		elif iRand == 2:
			#Married to the Alpha Wolf
			sTitle = sVerbTo + " to the " + sMaster
			if CoinFlip():
				if CoinFlip():
					sTitle += ": A " + self._getFMs_() + " Romance"
				else:
					sTitle += ": A BDSM Romance"
		elif iRand == 3:
			#The President's Girl
			sTitle = "The " + sMaster + "'s " + sGirl
			if CoinFlip():
				if CoinFlip():
					sTitle += "A BDSM Romance"
				else:
					sTitle += "A Hot Ménage"
		elif iRand == 4:
			#Seduced in the Bed of the Billionaire
			if CoinFlip():
				sTitle = sVerbTo + " in the Bed of the " + sMaster
			else:
				sTitle = sVerbBy + " in the Bed of the " + sMaster
		elif iRand == 5:
			#The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage
			sTitle = "The " + Masters.GetWord() + ", The " + sGirl + ", & The " + sMaster + ": "
			if CoinFlip():
				sTitle += "A Hot Ménage"
			else:
				sTitle += "A " + self._getFMs_() + " Romance"
		elif iRand == 6:
			#The Virgin's Secret Daddy Dom 
			sTitle = "The " + sGirl + "'s " + sMaster
		elif iRand == 7:
			#The Secretary and the Space Werewolf 
			sTitle = "The " + sGirl + " & the " + sMaster
			if CoinFlip():
				if CoinFlip():
					sTitle += "A BDSM Romance"
				else:
					sTitle += ": A " + self._getFMs_() + " Romance"
		elif iRand == 8:
			#Baby for the Stay-at-Home Manticore
			sTitle = "Baby for the " + sMaster 
			if CoinFlip():
				sTitle += ": A " + self._getFMs_() + " Romance"
		elif iRand == 9:
			#The Millionaire Sherrif's Virgin
			sTitle = "The " + sMaster + "'s " + sGirl
		elif iRand == 10:
			#Babysitter to the Billionaire Uniporn
			sTitle = sGirl + " to the " + sMaster
		elif iRand == 11:
			#Babysitter for the Billionaire Uniporn
			sTitle = sGirl + " for the " + sMaster
			if CoinFlip():
				if CoinFlip():
					sTitle += ": An " + self._getFMs_() + " Adventure"
				else:
					sTitle += ": A BDSM Romance"
			
		elif iRand == 12:
			#The Virgin Call-Girl's Gang Bang
			sTitle = "The " + sGirl + "'s Gang Bang: A " + self._getFMs_() + " Romance"
		elif iRand == 13:
			#The Small-Town Virgin's First Porno
			sTitle = "The " + sGirl + "'s First Porno"
			if CoinFlip():
				sTitle += ": An " + self._getFMs_() + " Adventure"
		elif iRand == 14:
			#The Small-Town Virgin's First Time
			sTitle = "The " + sGirl + "'s First Time"
			if CoinFlip():
				if CoinFlip():
					sTitle += ": An " + self._getFMs_() + " Romance"
				else:
					sTitle += ": A BDSM Romance"
		elif iRand == 15:
			sTitle = sVerbBy + ": "
			if CoinFlip():
				sTitle += "The " + sGirl + " & The " + sMaster
			else:
				sTitle += AddArticles(sGirl).title() + " Romance"
		else:
			pass
			
		return sTitle
		
class TweetReplyBuilder():
	def GetReply(self):
		sReply = ""
		sBookTitle = BookTitleBuilder().GetTitle()
		sSeller = BookSellers().GetWord()
		sSexyAdj = SexyAdjs().GetWord()
		
		sReply = "Look for my " + sSexyAdj + " story '" + sBookTitle + "' available soon on " + sSeller
		
		return sReply

class Punchline():
	Location = None
	MalePunchlines = []
	FemalePunchlines = []
	NeuterPunchlines = []
	
	BigEvent = None
	Exclamation = None 
	JobBlueCollar = None 
	JobWhiteCollar = None 
	JobWealthyMale = None 
	JobWealthyFemale = None 
	MaleFWB = None 
	FemaleFWB = None 
	MaleSO = None 
	FemaleSO = None 
	VerbSex = None 
	
	def __init__(self, Location = None):
		if not Location is None:
			self.Location = Location 
		else:
			self.Location = None
			
		self.BigEvent = Events()
		self.Exclamation = Exclamations()
		self.JobBlueCollar = people.JobBlueCollar()
		self.JobWhiteCollar = people.JobWhiteCollar()
		self.JobWealthyMale = people.JobWealthyMale()
		self.JobWealthyFemale = people.JobWealthyFemale()
		self.MaleFWB = people.MaleFWB()
		self.FemaleFWB = people.FemaleFWB()
		self.MaleSO = people.MaleSO()
		self.FemaleSO = people.FemaleSO()
		self.VerbSex = verbs.VerbSex()
		
		sHappyExclamation = ""
		sSadExclamation = ""
		sExclamation = ""
		
		if CoinFlip():
			sHappyExclamation = self.Exclamation.GetWord(bHappy = True).capitalize() + " "
			sSadExclamation = self.Exclamation.GetWord(bSad = True).capitalize() + " "
			sExclamation = self.Exclamation.GetWord().capitalize() + " "
		
		if not self.Location == None:
			#Female location-specific exclamations
			self.FemalePunchlines.append("'I've never done it " + Location.NamePrep + " before', she said.")
			self.FemalePunchlines.append("'Do you always take your girls " + Location.NamePrep + "?', she asked.")
			self.FemalePunchlines.append("'I'll bet you brought the last " + FemaleFWB.GetPerson() + " here too,' she said teasingly.")
			
			#Male location-specific exclamations
		
		#Female exclamations 
		self.FemalePunchlines.append("'This is not how I imagined spending " + self.BigEvent.GetWord() + "!' she said.")
		self.FemalePunchlines.append("'This has been the best " + self.BigEvent.GetWord(bRemoveMy = True) + " ever!' she said.")
		self.FemalePunchlines.append("'That was the best " + self.BigEvent.GetWord(bRemoveMy = True) + " gift ever!' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're the best " + self.JobWhiteCollar.GetPerson() +" ever!' she said.")
		self.FemalePunchlines.append("'You should know I'm married,' she said.")
		self.FemalePunchlines.append("'Don't you dare tell my mother about this,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I love you,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I'm in love with you,' she said.")
		self.FemalePunchlines.append("'You can't tell anyone that I'm a " + self.JobWealthyFemale.GetPerson() + ",' she said seriously.")
		self.FemalePunchlines.append("'We can't tell my " + self.MaleSO.GetWord() + " about this,' she said.")
		self.FemalePunchlines.append("'" + sSadExclamation + "My dress is completely ruined!' she said.")
		self.FemalePunchlines.append("'Before you ask, I already have a boyfriend,' she said, 'And he's not a " + self.JobBlueCollar.GetPerson() + " like you.'")
		self.FemalePunchlines.append("'It doesn't count as cheating on your " + self.MaleSO.GetWord() + " if you " + self.VerbSex.Present() + " a " + self.JobWealthyMale.GetPerson() + ", right?' she asked.")
		self.FemalePunchlines.append("'I can't let my " + self.MaleSO.GetWord() + " know that I'm screwing my " + self.JobBlueCollar.GetPerson() + "!' she said.")
		self.FemalePunchlines.append("'Hang on,' she said, 'I need to Snap Chat this.'")
		self.FemalePunchlines.append("'I usually only do this for money,' she said.")
		
		
		#Male exclamations
		self.MalePunchlines.append("'Happy " + self.BigEvent.GetWord(bRemoveMy = True) + "!' he said.")
		self.MalePunchlines.append("'We can't tell my " + self.FemaleSO.GetWord() + " about this,' he said.")
		self.MalePunchlines.append("'You should know I'm married,' he said.")
		self.MalePunchlines.append("'You can't tell anyone that I'm a " + self.JobWealthyMale.GetPerson() + ",' he said, seriously.")
		self.MalePunchlines.append("'Same time next Tuesday?' he asked.")
		self.MalePunchlines.append("'You remind me so much of my ex-wife,' he said.")
		
	def GetPunchline(self, gender):
		sPunchline = ""
		iRand = 0
		if gender == Gender.Male and not self.MalePunchlines is None and len(self.MalePunchlines) > 0:
			iRand = randint(0, len(self.MalePunchlines) - 1)
			sPunchline = self.MalePunchlines[iRand]
		elif gender == Gender.Female and not self.FemalePunchlines is None and len(self.FemalePunchlines) > 0:
			iRand = randint(0, len(self.FemalePunchlines) - 1)
			sPunchline = self.FemalePunchlines[iRand]
		elif gender == Gender.Neuter and not self.NeuterPunchlines is None and len(self.NeuterPunchlines) > 0:
			iRand = randint(0, len(self.NeuterPunchlines) - 1)
			sPunchline == self.NeuterPunchlines[iRand]
		else:
			pass
			
		return sPunchline
		
class PunchlineAfterSex(Punchline):
	def __init__(self, Location = None):
		if not Location is None:
			self.Location = Location 
		else:
			self.Location = None
			
		super().__init__(Location)
		
		sHappyExclamation = ""
		sSadExclamation = ""
		sExclamation = ""
		
		if CoinFlip():		
			sHappyExclamation = self.Exclamation.GetWord(bHappy = True).capitalize() + " "
			sSadExclamation = self.Exclamation.GetWord(bSad = True).capitalize() + " "
			sExclamation = self.Exclamation.GetWord().capitalize() + " "
		
		if not self.Location == None:
			#Female location-specific exclamations
			
			#Male location-specific exclamations
			self.MalePunchlines.append("'I can't believe I just did it with my " + self.FemaleFWB.GetPerson() + " " + Location.NamePrep + "!' he said.")
	
		#Female exclamations 
		self.FemalePunchlines.append("'" + sHappyExclamation + "That was amazing! What did you say your name was again?' she asked.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're so good, baby,' she said to her " + self.MaleFWB.GetPerson() + ".")	
		self.FemalePunchlines.append("'" + sHappyExclamation + "I can't believe I'm not a virgin anymore,' she said.")	
		self.FemalePunchlines.append("'Was this your first time " + self.VerbSex.Gerund() + " a " + self.JobWealthyFemale.GetPerson() + "?' she asked him.")	
		self.FemalePunchlines.append("'" + sExclamation + "What would my mother say if she knew that I was " + self.VerbSex.Gerund () + " a " + self.JobBlueCollar.GetPerson() + "?'. she asked.")
		self.FemalePunchlines.append("'Same time next Thursday?' she asked.")
		
		#Male exclamations 
		self.MalePunchlines.append("'You're even better than your sister,' he said.")
		self.MalePunchlines.append("'So is this a date?' he asked.")
	
		
		