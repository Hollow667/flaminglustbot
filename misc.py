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
			'bitcoin',
			'blockchain',
			'bot',
			'botlife',
			'botlife',
			'botlove',
			'eartg',
			'eartg',
			'erotica',
			'erotica',
			'filthy',
			'filthybot',
			'iamabot',
			'lprtg',
			'lprtg',
			'naughty',
			'naughtybot',
			'PleaseRT',
			'PleaseRT',
			'smut',
			'sorrynotsorry',
			'ssrtg',
			'ssrtg']
		
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
		'lordy',
		'oh goodness',
		'oh my',
		'shit',
		'sweet Mother Mary',
		'wow']
		
	def GetWord(self, bHappy = False, bSad = False, bExMk = True):
		sExclamation = ""
		iRand = 1
		
		sExclamation = super().GetWord()
		
		iRand = randint(1, 2)
		if iRand == 1 and not "oh " in sExclamation:
			sExclamation = "oh " + sExclamation
			
		iRand = randint(1, 2)
		if iRand == 1 and bHappy:
			sExclamation += " yes"
		elif iRand == 1 and bSad:
			sExclamation += " no"
			
		if bExMk:
			sExclamation += "!"
			
		return sExclamation
		
class SexyAdjs(WordList):
	List = ['dirty',
		'filthy',
		'hot',
		'naughty',
		'sexy',
		'steamy']

class BookSellers(WordList):
	List = ['Apple Books',
			'Amazon',
			'B&N',
			'Kobo',
			'Literotica',
			'Radish Fiction',
			'Smashwords',
			'WattPad']
			
class BookGirls(WordList):
	List = ['Amish Maiden',
			'Babysitter',
			'Call-Girl',
			'Co-ed',
			'Fashion Model',
			'Flight Attendant',
			'Handmaiden',
			'Harem Girl',
			'Hotwife',
			'Housewife',
			'Librarian',
			'Maiden',
			'Masseuse',
			'Midwife',
			'Milk Maid',
			'Nurse',
			'Pregnancy Surrogate',
			'Secretary',
			'Servant',
			'Sex Slave',
			'Sex Witch',
			'Single Mom',
			'Step-Daughter',
			'Step-Sister',
			'Sub',
			'Submissive',
			'Virgin',
			'Waitress',
			'Wife']
			
class BookGirlAdjs(WordList):
	List = ['BDSM',
		'Call-Girl',
		'Co-ed',
		'Easy',
		'Engaged',
		'High-Heeled',
		'Lesbian',
		'Married',
		'Pregnant',
		'Single',
		'Single Mom',
		'Submissive',
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
			'Hitman',
			'King',
			'Knight',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lesbian Harem',
			'Lipstick Lesbian',
			'Older Man',
			'Male Escort',
			'Male Stripper',
			'Man-o-taur',
			'Manor Lord',
			'Mantelope',
			'Manticore',
			'Marquis',
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
			'Sex Warlock',
			'Sheriff',
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
			'French',
			'Futanari',
			'Gazillionaire',
			'Highlander',
			'Hitman',
			'Horny',
			'Irish',
			'Italian',
			'Marine',
			'Millionaire',
			'MMA Fighter',
			'Mountain Man',
			'Multi-Millionaire',
			'Naked',
			'Navy Seal',
			'Older Man',
			'Pirate',
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
			'Trillionaire',
			'Viking',
			'Werewolf']
			
class BookVerbsBy(WordList):
	List = ['Blackmailed',
			'Bound',
			'Bred',
			'Claimed',
			'Conquered',
			'Charmed',
			'Cuckolded',
			'Dominated',
			'Enslaved',
			'Exposed',
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
			'Ravaged',
			'Seduced',
			'Spanked',
			'Shaved',
			'Taken',
			'Tempted',
			'Trained',
			'Watched']
			
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
		
		iRand = randint(1,5)
		sGirl = Girls.GetWord()
		sGirlAdj = GirlAdjs.GetWord()
		if iRand == 5:
			while sGirlAdj in sGirl:
				sGirlAdj = GirlAdjs.GetWord() 
			sGirl = sGirlAdj + " " + sGirl
			
		return sGirl
		
	def GetTitle(self):
		sTitle = ""
		
		Masters = BookMasters()
		VerbsBy = BookVerbsBy()
		VerbsTo = BookVerbsTo()
		
		sGirl = self.GetGirl()
		sMaster = self.GetMaster()
		sVerbBy = VerbsBy.GetWord()
		sVerbTo = VerbsTo.GetWord()
		
		iRand = randint(1,8)
		if iRand == 1:
			#Blackmailed by the Billionaire Mountain Man 
			sTitle = sVerbBy + " by the " + sMaster
		elif iRand == 2:
			#Married to the Alpha Wolf
			sTitle = sVerbTo + " to the " + sMaster
		elif iRand == 3:
			sTitle = "The " + sMaster + "'s " + sGirl
		elif iRand == 4:
			#Seduced in the Bed of the Billionaire 
			sTitle = sVerbTo + " in the Bed of the " + sMaster
		elif iRand == 5:
			#The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage
			sTitle = "The " + Masters.GetWord() + ", The " + sGirl + ", And The " + sMaster + ": A Hot Menage"
		elif iRand == 6:
			#The Virgin's Secret Daddy Dom 
			sTitle = "The " + sGirl + "'s " + sMaster
		elif iRand == 7:
			#The Secretary and the Space Werewolf 
			sTitle = "The " + sGirl + " & the " + sMaster
		elif iRand == 8:
			#Baby for the Stay-at-Home Manticore
			sTitle = "Baby for the " + sMaster 
		elif iRand == 9:
			#The Millionaire Sherrif's Virgin
			sTitle = "The " + sMaster + "'s " + sGirl
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
	
	def __init__(self, Location = None):
		self.Location = Location
		BigEvent = Events()
		Exclamation = Exclamations()
		JobBlueCollar = people.JobBlueCollar()
		JobWhiteCollar = people.JobWhiteCollar()
		JobWealthyMale = people.JobWealthyMale()
		JobWealthyFemale = people.JobWealthyFemale()
		MaleFWB = people.MaleFWB()
		FemaleFWB = people.FemaleFWB()
		VerbSex = verbs.VerbSex()
		
		sHappyExclamation = Exclamation.GetWord(bHappy = True).capitalize() + " "
		sSadExclamation = Exclamation.GetWord(bSad = True).capitalize() + " "
		sExclamation = Exclamation.GetWord().capitalize() + " "
		iCoinFlip = randint(1,2)
		
		if iCoinFlip == 2:
			sHappyExclamation = ""
			sSadExclamation = ""
			sExclamation = ""
		
		if not self.Location == None:
			#Female location-specific exclamations
			self.FemalePunchlines.append("'I've never done it " + Location.NamePrep + " before', she said.")
			self.FemalePunchlines.append("'Do you always take your girls " + Location.NamePrep + "?', she asked.")
			
			#Male location-specific exclamations
			self.MalePunchlines.append("'I can't believe I just did it with my " + FemaleFWB.GetPerson() + " " + Location.NamePrep + "!' he said.")
		
		#Female exclamations 
		self.FemalePunchlines.append("'" + sHappyExclamation + "That was amazing! What did you say your name was again?' she asked.")
		self.FemalePunchlines.append("'This is not how I imagined spending " + BigEvent.GetWord() + "!' she said.")
		self.FemalePunchlines.append("'This has been the best " + BigEvent.GetWord(bRemoveMy = True) + " ever!' she said.")
		self.FemalePunchlines.append("'That was the best " + BigEvent.GetWord(bRemoveMy = True) + " gift ever!' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're the best " + JobWhiteCollar.GetPerson() +" ever!' she said.")
		self.FemalePunchlines.append("'My son says when he grows up he wants to be a "+ JobWhiteCollar.GetPerson() + " like you!' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're so good, baby,' she said to her " + MaleFWB.GetPerson() + ".")
		self.FemalePunchlines.append("'You should know I'm married,' she said.")
		self.FemalePunchlines.append("'Don't you dare tell my mother about this,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I can't believe I'm not a virgin anymore,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I love you,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I'm in love with you,' she said.")
		self.FemalePunchlines.append("'I'll bet you brought the last " + FemaleFWB.GetPerson() + " here too,' she said teasingly.")
		self.FemalePunchlines.append("'Is this how a " + JobWealthyMale.GetPerson() + " treats a lady?' she asked.")
		self.FemalePunchlines.append("'You can't tell anyone that I'm a " + JobWealthyFemale.GetPerson() + ",' she said seriously.")
		self.FemalePunchlines.append("'We can't tell my boyfriend about this,' she said.")
		self.FemalePunchlines.append("'" + sSadExclamation + "My dress is completely ruined!' she said.")
		self.FemalePunchlines.append("'Was this your first time " + VerbSex.Gerund() + " a " + JobWealthyFemale.GetPerson() + "?' she asked him.")
		self.FemalePunchlines.append("'Before you ask, I already have a boyfriend,' she said, 'And he's not a " + JobBlueCollar.GetPerson() + " like you.'")
		self.FemalePunchlines.append("'" + sExclamation + "What would my mother say if she knew that I was " + VerbSex.Gerund () + " a " + JobBlueCollar.GetPerson() + "?'. she asked.")
		self.FemalePunchlines.append("'It doesn't count as cheating on your husband if you " + VerbSex.Present() + " a " + JobWealthyMale.GetPerson() + ", right?' she asked.")
		self.FemalePunchlines.append("'I can't let my " + MaleFWB.GetPerson() + " know that I'm screwing my " + JobBlueCollar.GetPerson() + "!' she said.")
		self.FemalePunchlines.append("'Hang on,' she said, 'I need to Snap Chat this.'")
		self.FemalePunchlines.append("'I usually only do this for money,' she said.")
		self.FemalePunchlines.append("'Same time next Thursday?' she asked.")
		
		#Male exclamations
		self.MalePunchlines.append("'Happy " + BigEvent.GetWord(bRemoveMy = True) + "!' he said.")
		self.MalePunchlines.append("'We can't tell my girlfriend about this,' he said.")
		self.MalePunchlines.append("'You should know I'm married,' he said.")
		self.MalePunchlines.append("'You can't tell anyone that I'm a " + JobWealthyMale.GetPerson() + ",' he said, seriously.")
		self.MalePunchlines.append("'Same time next Tuesday?' he asked.")
		
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
			
			
			
		
		
	
		
		