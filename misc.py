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
	List = ['50shades',
			'amwriting',
			'BDSM',
			#'bitcoin',
			#'blockchain',
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
			#'litecoin',
			'lovestory',
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
			'twitterbot',
			'wprtg']
		
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
		
class Gobs(WordList):
	List = ['beads', 
		'drops', 
		'globules', 
		'gobs', 
		'pearls', 
		'ropes', 
		'strings', 
		'trails']
		
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
	List = ['Airline Stewardess',
			'Amish Maiden',
			'Anal Virgin',
			'Babysitter',
			'Bikini Model',
			'Bimbo',
			'Blonde',
			'Brat',
			'Bride',
			'Bride',
			'Bridesmaid',
			'BBW',
			'Call-Girl',
			'Co-ed',
			'Concubine',
			'Escort',
			'Fashion Model',
			'Farmer\'s Daughter',
			'Flight Attendant',
			'Futa',
			'Girlfriend',
			'Governess',
			'Handmaiden',
			'Harem Girl',
			'Hotwife',
			'Housewife',
			'House Maid',
			'Flight Attendant',
			'French Maid',
			'Intern',
			'Lady',
			'Librarian',
			'Lingerie Model',
			'Maid',
			'Maiden',
			'Masseuse',
			'Mature Woman',
			'MILF',
			'Milk Maid',
			'Momma',
			'Nanny',
			'Nurse',
			'Older Woman',
			'Pastor\'s Wife',
			'Princess',
			'Princess',
			'Redhead',
			'Sex Surrogate',
			'Secretary',
			'Secretary',
			'Sex Slave',
			'Sex Witch',
			'Schoolgirl',
			'Single Mom',
			'Small-Town Girl',
			'Slut',
			'Step-Daughter',
			'Submissive',
			'Teacher',
			'Virgin',
			'Wallflower',
			'Waitress',
			'Wet Nurse',
			'Whore',
			'Wife',
			'Woman']
			
class BookGirlAdjs(WordList):
	List = ['Amish',
		'Anal',
		'Bashful',
		'BBW',
		'BDSM',
		'Bi-Curious',
		'Bimbo',
		'Black',
		'Blonde',
		'Call-Girl',
		'Chaste',
		'Christian',
		'Co-ed',
		'Concubine',
		'Conservative',
		'Country',
		'Curvy',
		'Divorced',
		'Ebony',
		'Fertile',
		'Futa',
		'Harem',
		'Hotwife',
		'High-Heeled',
		'Innocent',
		'Innocent',
		'Intern',
		'Kept',
		'Kinky',
		'Lactating',
		'Lesbian',
		'Live-in',
		'Married',
		'MILF',
		'Naked',
		'Naked',
		'Naughty',
		'Nubile',
		'Nude',
		'Nudist',
		'Nursing',
		'Pregnant',
		'Redhead',
		'Servant',
		'Sex',
		'Shy',
		'Single',
		'Single Mom',
		'Small-Town',
		'Submissive',
		'Taboo',
		'Teen',
		'Teenage',
		'Virgin',
		'Virgin',
		'Virgin',
		'Virgin',
		'Young']

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
			'Daddy',
			'Daddy Dom',
			'Defensive Lineman',
			'Dildo Designer',
			'Dinosaur',
			'Doctor',
			'Dom',
			'Dominatrix',
			'Duke',
			'Duke',
			'Futanari',
			'Gay-for-Pay Porn Star',
			'Gazillionaire',
			'Gentleman',
			'Goat Man',
			'Goat Men',
			'Hitman',
			'Incubus',
			'Fire Fighter',
			'Jet Fighter Pilot',
			'King',
			'Knight',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lesbian Harem',
			'Lesbian MILF',
			'Lipstick Lesbian',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
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
			'Porn Star',
			'President',
			'Prince',
			'Professor',
			'Quarterback',
			'Rock Star',
			'Shah',
			'Sex Addict',
			'Sex Warlock',
			'Sheikh',
			'Sheriff',
			'Sorcerer',
			'Spy',
			'Surfer',
			'S.W.A.T. Team',
			'Trillionaire',
			'Viking',
			'Viking Hoard',
			'Uniporn',
			'Vampire',
			'Vampire Coven',
			'Voyeur',
			'Werewolf',
			'Werewolf Pack',
			'Widower']
			
class BookMasterAdjs(WordList):
	List = ['Alpha',
			'Bad Boy',
			'Bitcoin Billionaire',
			'Biker',
			'Billionaire',
			'Black',
			'Cowboy',
			'Defensive Lineman',
			'Dinosaur',
			'Ebony',
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
			'Nudist',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Pirate',
			'Playboy',
			'Porn Star',
			'Rebel',
			'Rock Star',
			'Savage',
			'Scottish',
			'Secret',
			'Sex Addict',
			'Shape-Shifting',
			'Single Dad',
			'Space',
			'Spanish',
			'Stay-at-Home',
			'Stripper',
			'Superstar',
			'Surfer',
			'S.W.A.T. Team',
			'Trillionaire',
			'Viking',
			'Well-hung',
			'Werewolf',
			'Wicked',
			'Widowed']
			
class BookVerbsBy(WordList):
	List = ['Anally Deflowered',
			'Annally Deflowered in Public',
			'Blackmailed',
			'Bound',
			'Bred',
			'Captured',
			'Claimed',
			'Claimed',
			'Claimed Hard',
			'Claimed in Public',
			'Conquered',
			'Charmed',
			'Cuckolded',
			'Deflowered',
			'Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Enslaved',
			'Exposed in Public',
			'Forced',
			'Hotwifed',
			'Humiliated',
			'Hunted For Food',
			'Impregnated',
			'Kept',
			'Knocked Up',
			'Mastered',
			'Owned',
			'Pleasured',
			'Pleasured in Public',
			'Punished',
			'Punished in Public',
			'Ravished',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Sold',
			'Sold',
			'Spanked',
			'Spanked in Public',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Taken',
			'Taken',
			'Taken Hard',
			'Taken Hard in Public',
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
			
# I really really like the random book titles. See if you can tell! ;-P
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
		
		Titles = []
		
		# Blackmailed by the Billionaire Mountain Man 
		sTitle = sVerbBy + " by the " + sMaster
		Titles.append(sTitle)
		# =========================

		# Married to the Alpha Wolf
		sTitle = sVerbTo + " to the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A " + self._getFMs_() + " Romance"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
		
		# The President's Girl
		sTitle = "The " + sMaster + "'s " + sGirl
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A BDSM Romance"
			else:
				sTitle += ": A Hot Ménage"
		Titles.append(sTitle)
		# =========================
				
		# Seduced in the Bed of the Billionaire
		if CoinFlip():
			sTitle = sVerbTo + " in the Bed of the " + sMaster
		else:
			sTitle = sVerbBy + " in the Bed of the " + sMaster
		Titles.append(sTitle)
		# =========================
				
		# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage
		sTitle = "The " + Masters.GetWord() + ", The " + sGirl + ", & The " + sMaster + ": "
		if CoinFlip():
			sTitle += "A Hot Ménage"
		else:
			sTitle += "A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Virgin's Secret Daddy Dom 
		sTitle = "The " + sGirl + "'s " + sMaster
		Titles.append(sTitle)
		# =========================
				
		# The Secretary and the Space Werewolf 
		sTitle = "The " + sGirl + " & the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A BDSM Romance"
			else:
				sTitle += ": A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# Baby for the Stay-at-Home Manticore
		sTitle = "Baby for the " + sMaster 
		if CoinFlip():
			sTitle += ": A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Millionaire Sherrif's Virgin
		sTitle = "The " + sMaster + "'s " + sGirl
		Titles.append(sTitle)
		# =========================
				
		# Babysitter to the Billionaire Uniporn
		sTitle = sGirl + " to the " + sMaster
		Titles.append(sTitle)
		# =========================
				
		# Babysitter for the Billionaire Uniporn
		sTitle = sGirl + " for the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": An " + self._getFMs_() + " Adventure"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Virgin Call-Girl's Gang Bang
		sTitle = "The " + sGirl + "'s Gang Bang: A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Small-Town Virgin's First Porno
		sTitle = "The " + sGirl + "'s First Porno"
		if CoinFlip():
			sTitle += ": An " + self._getFMs_() + " Adventure"
		Titles.append(sTitle)
		# =========================
				
		# The Small-Town Virgin's First Time
		sTitle = "The " + sGirl + "'s First Time"
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A " + self._getFMs_() + " Romance"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# Enslaved: The Ebony Older Woman & The Duke 
		sTitle = sVerbBy + ": "
		if CoinFlip():
			sTitle += "The " + sGirl + " & The " + sMaster
		else:
			sTitle += AddArticles(sGirl).title() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# Full Frontal for the Shy Amish Virgin: A BDSM Romance
		if CoinFlip():
			sTitle = "Full Frontal Nudity for the "
			if CoinFlip():
				sTitle += sMaster
			else:
				sTitle += sGirl
		else:
			sTitle = "Naked for the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": An " + self._getFMs_() + " Adventure"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# I Was Stripped In Public, And I Liked It
		sTitle = "I Was " + sVerbBy
		if not "in public" in sVerbBy.lower():
			sTitle += " By A " + sMaster
		sTitle += ", And I Liked It"
		Titles.append(sTitle)
		# =========================
				
		# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
		sTitle = sVerbBy  + " by "
		sTitle += "the " + sMaster + ": A " + sGirl + " Story"
		Titles.append(sTitle)
		# =========================
				
		# The Amish Virgin and the Taboo MILF: A Lesbian Love Story 
		sTitle = "The " + sGirl + " and the " + self.GetGirl()
		if CoinFlip():
			sTitle += ": A Lesbian Love Story"
		else:
			sTitle += ": A Secret Lesbian Affair"
		Titles.append(sTitle)
		# =========================
		
		# Deflowered Live on the Internet: An Amish Futa Princess Experience 
		sTitle = "Deflowered Live"
		if CoinFlip():
			sTitle += "! "
		else:
			if CoinFlip():
				sTitle += " on the Interet: "
			else:
				sTitle += " on Television: "
		sTitle += AddArticles(sGirl) + " Experience"
		Titles.append(sTitle)
		# =========================
		
		# Here Cums The Bride: The Porn Star Pope & The Bi-Curious Christian Milk Maid 
		sTitle = "Here Cums The Bride: The " + sMaster + " & The "
		while 'bride' in sGirl.lower():
			sGirl = self.GetGirl()
		sTitle += sGirl
		Titles.append(sTitle)
		# =========================
		
		# Hotwife for Daddy: A BDSM Romance 
		sTitle = sGirl + " for Daddy: "
		if CoinFlip():
			sTitle += "A BDSM Romance"
		else:
			sTitle += "An " + self._getFMs_() + " Adventure"
		Titles.append(sTitle)
		# =========================
		
		sTitle = Titles[randint(0, len(Titles) - 1)]
		
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
	
		
		