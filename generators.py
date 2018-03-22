# Utilities module

import sys, threading, traceback
from random import *
from util import *
from bodyparts import *
from verbs import *
from misc import *
from scenes import *
from names import *
from locations import *
from people import *

Q_SIZE = 5

HistoryQ = []

def GetTweet(bTest, iGeneratorNo = MAX_GENERATOR_NO):
	Tweet = [0,""]
	sTweet = ""
	iSwitch = 999

	iRandMin = 0
	iRandMax = iGeneratorNo
	
	if bTest:
		iRandMin = iGeneratorNo
	
	iSwitch = randint(iRandMin, iRandMax)
	while not bTest and iSwitch in HistoryQ:
		iSwitch = randint(iRandMin, iRandMax)
	
	HistoryQ.insert(0, iSwitch)
	if len(HistoryQ) > Q_SIZE:
		HistoryQ.pop()
	
	if iSwitch == 0:
		sTweet = GeneratorPromo().GenerateTweet()
	elif iSwitch == 1:
		sTweet = Generator1().GenerateTweet()
	elif iSwitch == 2:
		sTweet = Generator2().GenerateTweet()
	elif iSwitch == 3:
		sTweet = Generator3().GenerateTweet()
	elif iSwitch == 4:
		sTweet = Generator4().GenerateTweet()
	elif iSwitch == 5:
		sTweet = Generator5().GenerateTweet()
	elif iSwitch == 6:
		sTweet = Generator6().GenerateTweet()
	elif iSwitch == 7:
		sTweet = Generator7().GenerateTweet()
	elif iSwitch == 8:
		sTweet = Generator8().GenerateTweet()
	elif iSwitch == 9:
		sTweet = Generator9().GenerateTweet()
	elif iSwitch == 10:
		sTweet = Generator10().GenerateTweet()
	elif iSwitch == 11:
		sTweet = Generator11().GenerateTweet()
	elif iSwitch == 12:
		sTweet = Generator12().GenerateTweet()
	elif iSwitch == 13:
		sTweet = Generator13().GenerateTweet()
	elif iSwitch == 14:
		sTweet = Generator14().GenerateTweet()
	elif iSwitch == 15:
		sTweet = Generator15().GenerateTweet()
	elif iSwitch == 16:
		sTweet = Generator16().GenerateTweet()
	elif iSwitch == 17:
		sTweet = Generator17().GenerateTweet()
	elif iSwitch == 18:
		sTweet = Generator18().GenerateTweet()
	elif iSwitch == 19:
		sTweet = Generator19().GenerateTweet()
	elif iSwitch == 20:
		sTweet = Generator20().GenerateTweet()
	elif iSwitch == 21:
		sTweet = Generator21().GenerateTweet()
	elif iSwitch == 22:
		sTweet = Generator22().GenerateTweet()
	elif iSwitch == 23:
		sTweet = Generator23().GenerateTweet()
	elif iSwitch >= 24 and iSwitch < 26:
		sTweet = Generator24().GenerateTweet()
	elif iSwitch >= 26 and iSwitch < 29:
		sTweet = Generator25().GenerateTweet()
	elif iSwitch >= 29 and iSwitch < 32:
		sTweet = Generator26().GenerateTweet()
	elif iSwitch == 32:
		sTweet = Generator27().GenerateTweet()
	elif iSwitch >= 33 and iSwitch < 36:
		sTweet = Generator28().GenerateTweet()
	elif iSwitch >= 36 and iSwitch < 39:
		sTweet = Generator29().GenerateTweet()
	elif iSwitch == 39:
		sTweet = Generator30().GenerateTweet()
	elif iSwitch == 40:
		sTweet = Generator31().GenerateTweet()
	elif iSwitch == 41:
		sTweet = Generator32().GenerateTweet()
	elif iSwitch == 42:
		sTweet = Generator33().GenerateTweet()
	elif iSwitch == 43:
		sTweet = Generator34().GenerateTweet()
	elif iSwitch == 44:
		sTweet = Generator35().GenerateTweet()
	#elif iSwitch == ??:
		#He opened the door and his heart skipped a beat. Angela was lying on the bed naked. [Describe] She opened her naked legs, reached down and spread her gleaming pussy lips. 
	#elif iSwitch == ??:
		#I still love you, Veronica, he said, even after all these years. I love you too, Steve, said Veronica. I've loved you since the first time you titty fucked me in the men's bathroom
	#elif iSwitch == ??:
		#Raoul entered, wearing a white robe. He whipped the towel off Rosanna, exposing her naked form. He began to gently massage her {body parts}. Rosanna opened her eyes. His robe was now open, exposing his massive swollen
	#elif iSwitch == ??:
		#'Kylie! Hi!' he said to the barista. 'You two know each other?' Sam's girlfriend asked. 'Oh yes,' said Kylie. 'Sam sucked my titties back in college.'
	else:
		print("iSwitch not found: " + str(iSwitch))
		
	return sTweet
	
def IsTweetTooLong(sTweet):
	bTooLong = True
	
	if len(sTweet) <= MAX_TWITTER_CHARS:
		bTooLong = False 
	
	return bTooLong
	
def ChopTweet(sTweet, sPrefix):
	Tweets = []
	iTargetLen = MAX_TWITTER_CHARS - 4
	iTweetNo = 1
	
	iLastChar = iTargetLen
	sTweet = sPrefix + str(iTweetNo) + ") " + sTweet
	while not sTweet[iLastChar].isspace():
		iLastChar = iLastChar - 1
	
	Tweets.append(sTweet[0:iLastChar])
	sTweet = sTweet[iLastChar + 1:]
	iTweetNo = iTweetNo + 1
	sTweet = str(iTweetNo) + ") " + sTweet
		
	while len(sTweet) > iTargetLen:
		iLastChar = iTargetLen
		
		while not sTweet[iLastChar].isspace():
			iLastChar = iLastChar - 1
			
		Tweets.append(sTweet[0:iLastChar])
		sTweet = sTweet[iLastChar + 1:]
		iTweetNo = iTweetNo + 1
		sTweet = str(iTweetNo) + ") " + sTweet
		
	Tweets.append(sTweet)
	
	return Tweets

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets
	
def GetChoppedTweets(bTest, iGeneratorNo = MAX_GENERATOR_NO, sPrefix = ""):
	Tweets = [1]
	sTweetStr = ""
	
	print("Prefix is [" + sPrefix + "]")
	sTweetStr = GetTweet(bTest, iGeneratorNo)
	print(sTweetStr)
	if len(sTweetStr) > 0:
		if IsTweetTooLong(sPrefix + sTweetStr):
			Tweets = ChopTweet(sTweetStr, sPrefix)
		else:
			Tweets[0] = sPrefix + sTweetStr
		Tweets = AddHashtag(Tweets)	
	else: 
		Tweets[0] = sTweetStr

	return Tweets

class Generator():
	MaleBodyparts = None 
	FemBodyParts = None 
	Semen = None
	
	Event = None 
	Exclamation = None 
	Punchline = None 
	
	MaleName = None
	FemaleName = None
	BadGirlName = None
	
	VEjac = None 
	VForeplay = None
	VMakeLove = None 
	VMoan = None
	VSex = None
	VThrust = None
	
	MFWB = None 
	FFWB = None 
	
	BlueCollar = None 
	WhiteCollar = None 
	WealthyMan = None 
	WealthyWoman = None
	
	CreamPieScene = None
	
	def __init__(self):
		self.MaleBodyParts = BodyMale()
		self.FemBodyParts = BodyFemale()
		self.Semen = Semen()
		
		self.Event = misc.Events()
		self.Exclamation = misc.Exclamations()
		self.Punchline = misc.Punchline()
	
		self.FemaleName = NamesFemale()
		self.MaleName = NamesMale()
		self.BadGirlName = BadGirlNames()
		
		self.VEjac = VerbEjaculate()
		self.VForeplay = VerbForeplay()
		self.VMakeLove = VerbMakeLove()
		self.VMoan = VerbMoan()
		self.VSex = VerbSex()
		self.VThrust = VerbThrust()
		
		self.MFWB = MaleFWB()
		self.FFWB = FemaleFWB()
		
		self.WealthyMan = JobWealthyMale()
		self.WealthyWoman = JobWealthyFemale()
		self.WhiteCollar = JobWhiteCollar()
		self.BlueCollar = JobBlueCollar()
	
	def GenerateTweet(self):
		return ""
		
class Generator1(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		# The baron desecrated Jacinda's well-used muffin with his thick pole.	
		sVerb = self.VForeplay.Present()
		sTweet = "The " + self.WealthyMan.GetPerson() + " " + self.VThrust.Past() + " " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n'" + sVerb.capitalize() + " my " + self.FemBodyParts.Breasts.RandomDescription() + "!' she " + self.VMoan.Past() + ". '" + sVerb.capitalize() + " them and fill me with your " + self.Semen.FloweryDescription() + "!'"
		
		return sTweet
		
class Generator2(Generator):
	# Spreading open her supple buttocks with his rough hands, he desecrated her well-used anus with his erect boner. 'Fuck me,
	# Jordan!' she screamed. 'Pound me like your wife!'	
		
	def GenerateTweet(self):
		sTweet = ""
		
		self.MaleBodyParts = BodyMale()
		self.FemBodyParts = BodyFemale()
		self.MaleName = NamesMale()
		self.FemaleName = NamesFemale() 
		self.VThrust = VerbThrust()
		
		sTweet = "Spreading open " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.Ass.RandomDescription() + " with his rough hands, he " + self.VThrust.Past() + " her " + self.FemBodyParts.Ass.Anus.RandomDescription() + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n"
		sTweet += "'Do me, " + self.MaleName.FirstName() + "!\' she " + self.VMoan.Past() + ". '" + self.VThrust.Present().capitalize() + " me like I'm your " + self.FFWB.GetPerson() + "!'"
		
		return sTweet

class Generator3(Generator):
	# 'Please, no!' she said, squirming as he bayonetted her pink cooch. 'Not while my yoga teacher is watching!'
	def GenerateTweet(self):
		sTweet = ""
			
		sTweet = "'Please, no!' " + self.FemaleName.FirstName() + " " + self.VMoan.Past() + ", squirming with pleasure as " + self.MaleName.FirstName() + " " + self.VThrust.Past() + " her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". 'Not while my " + self.MFWB.GetPerson() +" is watching!'"
		
		return sTweet

class Generator4(Generator):
	# 'You may cum inside my womanhood if you like', she instructed him, 'But only my photographer is allowed to bayonette my sphincter.'	
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = "'You may cum inside my " + self.FemBodyParts.Vagina.ShortDescription() + " if you like', " + self.FemaleName.FirstName() + " instructed him, 'But only my " + self.MFWB.GetPerson() + " is allowed to " + self.VThrust.Present() + " my " + self.FemBodyParts.Ass.Anus.RandomDescription() + "'."
		
		return sTweet
		
class Generator5(Generator):
	# 'Oh, Leon,' she moaned, 'I'm so thirsty for your glossy spunk!' 'But Ophelia,' he said, 'You're my mother-in-law!'
	def GenerateTweet(self):
		sTweet = ""
			
		sTweet = "'Oh, " + self.MaleName.FirstName() + ",' she " + self.VMoan.Past() + " in his " + self.MaleBodyParts.Arms.MediumDescription() + ", 'I'm so thirsty for your " + self.Semen.RandomDescription() + "!'\n\n'But " + self.FemaleName.FirstName() + ",' he said, 'You're my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
class Generator6(Generator):
	# 'You don't have to hide the truth from me, Honey,' he said, 'Tom is a successful opthamologist and I'm just a lowly roadie!' 
	# 'That's true,' she said, 'But YOU have a 8 1/2 inch fuck-pole!'	
	def GenerateTweet(self):
		sTweet = ""
		
		sRivalName = self.MaleName.FirstName()
		sTweet = "'You don't have to hide the truth from me, " + self.FemaleName.FirstName() + ",' he said, '" + sRivalName + " is a successful " + self.WhiteCollar.GetPerson() + " and I'm just a lowly " + self.BlueCollar.GetPerson() + "!'\n\n'I don't care about " + sRivalName + ",' she said, 'You're the one I want. And anyway, you have a " + str(randint(8, 12)) + " 1/2 inch " + self.MaleBodyParts.Penis.ShortDescription() + "!'"
		
		return sTweet
		
class Generator7(Generator):
	# Charity bit her lip as Tristan fondled her heaving bosoms. 'Oh god,' she said, 'What would my pastor say if he saw that I was letting my pool boy pump into my crack?'	
	
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		
		sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on " + Location.SittingOn + ", her " + self.FemBodyParts.Breasts.RandomDescription() + " heaving as " + self.MaleName.FirstName() + " lubed up her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ". '" + self.Exclamation.GetWord().capitalize() + "' she " + self.VMoan.Past() + ", 'What would Father " + self.MaleName.FirstName() + " say if he knew that my " + self.MFWB.GetPerson() + " was " + self.VThrust.Gerund() + " my " + self.FemBodyParts.Ass.ShortDescription() + " " + Location.NamePrep + "?'"
		
		return sTweet

class Generator8(Generator):
	#Bianca bit her lip as he caressed her youthful thighs. 'Ferdinand!' she said, 'My urologist is in the next room!' 
	#'Should we invite him?' he asked innocently, inserting a finger into her love channel.	
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location(InOut = LocInOutType.Indoors)
		
		sBoyfriendName = self.MaleName.FirstName()
		sTweet = self.FemaleName.FirstName() + " bit her lip as he " + self.VForeplay.Past() + " her " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " " + Location.NamePrep + ". "
		sTweet += "'" + sBoyfriendName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson() + " is right outside!'\n\n'Do you think he'd like to join us?' " + sBoyfriendName + " asked innocently, inserting a finger into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
		
		return sTweet
		
class Generator9(Generator):
	# 'What?' she said. 'Hasn't a girl ever let you fuck her oiled-up coconuts with your meat pole before?''Only my dad's girlfriend,' he replied.
	def GenerateTweet(self):
		sTweet = ""
			
		sTweet = "'What?' she asked. 'Hasn't a girl ever let you fuck her big, oiled-up " + self.FemBodyParts.Breasts.ShortDescription() + " with your " + self.MaleBodyParts.Penis.RandomDescription() + " before?'\n\n'Only my " + self.FFWB.GetPerson() + ",' " + self.MaleName.FirstName() + " replied."
		
		return sTweet
		
class Generator10(Generator):
	#'Oh lord, what a day it has been,' said the dutchess. Ripping open her blouse, she exposed her massive double-D mammaries. 'Come, my little fry cook, I need you to nibble on my buns and then to cover my hard nipples in your salty man jam.'
	def GenerateTweet(self):
		sTweet = ""

		sTweet = "'" + self.Exclamation.GetWord(bExMk = False).capitalize() + ", what a day it has been,' said the " + misc.WomanAdjs().GetWord() + " " + self.WealthyWoman.GetPerson() +". Ripping open her blouse, she exposed her " + self.FemBodyParts.Breasts.RandomDescription() + " to him. 'Come, my little " + self.BlueCollar.GetPerson() + ". I need you to " + self.VForeplay.Present() + " my " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " and cover my " + self.FemBodyParts.GetRandomBodyParts(1, False, True)[0] + " in your "+ self.Semen.RandomDescription() + ".'"
		
		return sTweet
		
class Generator11(Generator):
	# 'Oh God, Julia,' he said, 'You are so beautiful. I love your supple skin, your sumptuous hips, your perfect thighs, the way
	# you look with my ballsack in your mouth.'
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = "'" + self.Exclamation.GetWord(bExMk = False, bHappy = True).capitalize() + ", " + self.FemaleName.FirstName() + ",' he " + self.VMoan.Past() + ", 'You are so beautiful. I love your "
		for part in self.FemBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False):
			sTweet += part + ", "
		sTweet += "and the way you look with my " + self.MaleBodyParts.Penis.GetRandomPenisPart() + " in your " + self.FemBodyParts.Mouth.RandomDescription() + ".'"
		
		return sTweet
		
class Generator12(Generator):
	# Ginger's robe fell to the floor, and his heart skipped a beat. She had a shapely form with ripe boobs, wide hips, and a 
	# well-used hole. "I can't believe you're my sister," he said.	
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = self.FemaleName.FirstName() + "'s robe fell to the floor, and his heart skipped a beat. She had "
		
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += AddArticles(part) + ", "
			else:
				sTweet += "and " + AddArticles(part) 
		sTweet += ".\n\n'" + self.Exclamation.GetWord(bHappy = True).capitalize() + " I can't believe you're my " + self.FFWB.GetPerson() + "!' he " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator13(Generator):	
	# 'Oh thank God Christina,' he gasped. 'You saved me. How can I ever repay you?' Christina bent over and pulled down her panties,
	# revealing her pert bum. 'You can start by licking my starfish,' she said.
	def GenerateTweet(self):
		sTweet = ""
		
		iRand = randint(1,3)
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "'Oh thank God " + sGirlfriendName + ",' he said to the woman with the " + self.FemBodyParts.Eyes.MediumDescription() + " and " + self.FemBodyParts.Hair.RandomDescription(bAllowShortDesc = False) + ". 'You saved me. How can I ever repay you?'\n\n" 
		if iRand == 1:
			sTweet += sGirlfriendName + " bent over and pulled down her panties, revealing her " + self.FemBodyParts.Ass.RandomDescription() + ".\n\n"
			sTweet += "'You can start by licking my " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' she said."
		elif iRand == 2:
			sGirlfriendName + " bent over and pulled down her panties, revealing her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ".\n\n"
			sTweet += "'You can start by eating out my filthy little " + self.FemBodyParts.Vagina.ShortDescription() + ",' she said."
		else:
			sGirlfriendName + " bent over and pulled down her panties, revealing her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ".\n\n"
			sTweet += "'You can start by fisting my " + self.FemBodyParts.Vagina.InnerVag.ShortDescription() + ",' she said."
		
		return sTweet
	
class Generator14(Generator):
	# 'Oh Julian,' she said, 'I've never been with a duke before.'
	# 'Fear not, my love,' he said, as he began to gently fuck her bunghole."
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = "'Oh " +self.MaleName.FirstName() + ",' she said, 'I've never been with a " + self.WealthyMan.GetPerson() + " before.'\n\n"
		sTweet += "'Fear not, my darling love, I would never hurt you,' he said as he began to " + self.VMakeLove.Present() + " her " + self.FemBodyParts.GetRandomHole() + " with his " + str(randint(8,14)) + "\" " + self.MaleBodyParts.Penis.RandomDescription() + "."
		
		return sTweet
		
class Generator15(Generator):
	# 'Vance, my love, where are you?' called Anjelica from the next room. Vance looked down at Veronica. Her dazzling blue eyes 
	# were locked on his as she wrapped her hungry mouth around his massive meat pole. "I'll just be a minute dear," Vance replied.
	def GenerateTweet(self):
		sTweet = ""
				
		sBoyfriendName = self.MaleName.FirstName()
		sTweet = "'" + sBoyfriendName + ", my love, where are you?' called " + self.FemaleName.FirstName() + " from the next room.\r\n"
		sTweet += sBoyfriendName + " looked down at " + self.FemaleName.FirstName() + ". Her " + self.FemBodyParts.Eyes.RandomDescription() + " were locked on his as she wrapped her " + self.FemBodyParts.Mouth.RandomDescription() + " around his " + self.MaleBodyParts.Penis.FloweryDescription() + ".\n\n"
		sTweet += "'I'll just be a minute dear,' " + sBoyfriendName + " replied."
		
		return sTweet
		
class Generator16(Generator):
	# Devon squeezed and sucked on Sabrina's luscious double-D mammaries as he fingered her clit and jackhammered her willing cunt 
	# hole. 'My god,' whispered Grant, stroking his meat sword, 'I can't believe I'm watching my wife fuck an opthamologist!'"
		
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = self.MaleName.FirstName() + " squeezed and sucked on " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.Breasts.RandomDescription() + " as he fingered her " + self.FemBodyParts.Vagina.Clitoris.RandomDescription() + " and " + self.VThrust.Past() + " her " + self.FemBodyParts.GetRandomHole() + ".\n\n"
		sTweet += "'" + self.Exclamation.GetWord(bHappy = True).capitalize() + "' " + self.VMoan.Past() + " " + self.MaleName.FirstName() + ", stroking his " + self.MaleBodyParts.Penis.RandomDescription() + " as he looked on, 'I can't believe I'm watching my wife " + self.VSex.Present() + " " + AddArticles(self.WhiteCollar.GetPerson()) + "!'"
		
		return sTweet
		
class Generator17(Generator):
	# Charity's eyes were wide as she cupped his dangling nutsack. 'Does every opthamologist have one like this?' she asked. 
	# 'No darling,' said Brad. 'Not every opthamologist has a 9 1/2 inch meat sword. Now play with my testicles while you rub the swollen head.'
	def GenerateTweet(self):
		sTweet = ""
		
		sWhiteCollarJob = self.WhiteCollar.GetPerson()
		sTweet = self.FemaleName.FirstName() + " stared with innocent " + self.FemBodyParts.Eyes.MediumDescription() + " at his " + self.MaleBodyParts.Penis.MediumDescription() + ". 'Does every " + sWhiteCollarJob + " have a... thing like this?' she asked.\n\n"
		sTweet += "'No darling,' said " + self.MaleName.FirstName() + " chuckling. 'Not every " + sWhiteCollarJob + " has a " + str(randint(8, 12)) + "\" " + self.MaleBodyParts.Penis.ShortDescription() + ". Now massage my " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + " while you suck on my " + self.MaleBodyParts.Penis.Head.ShortDescription() + ".'"
		
		return sTweet
		
class Generator18(Generator):
	# "'Jacinda, my dear, I wrote you a poem,' he said. 'What is it about?' asked Jacinda. 'It's about you, my love: your golden 
	# hair, your generous tits, your smooth legs, your dangling labia.' 'Oh Brad!' she sighed."
	def GenerateTweet(self):
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "'" + sGirlfriendName + ", my dear, I wrote you a poem,' he said.\n\n"
		sTweet += "'What about?' she asked.\n\n"
		sTweet += "'It's about you, my love,' he said. 'It's about your "
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = True)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "& your " + part
		sTweet += ".'\n\n"
		sTweet += "'Oh " + self.MaleName.FirstName() + "!' she sighed."
		
		return sTweet
		
class Generator19(Generator):
	#Unaware Roxanne was watching him, Nicolas pulled his tshirt and jeans off, revealing his broad shoulders, powerful chest, and sinewy thighs. But what made Roxanne's mouth water was the massive, throbbing tool between his legs.	
	def GenerateTweet(self):
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "Unaware " + sGirlfriendName + " was watching him, " + self.MaleName.FirstName() + " pulled his tshirt and jeans off, revealing his "
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and " + part
		sTweet += ". But what made her mouth water was the " + self.MaleBodyParts.Penis.FloweryDescription() + " dangling between his legs."
		
		return sTweet
		
class Generator20(Generator):
	#Xavier approached the bed, completely naked. A thrill ran through Constance at the sight of his broad shoulders, powerful chest, sinewy thighs, muscular buttocks and swollen man meat. She could hardly believe that in a few minutes this man would be stuffing her virgin pussy.
	def GenerateTweet(self):
		sTweet = ""

		sTweet = self.MaleName.FirstName() + " approached the bed completely naked. A thrill ran through " + self.FemaleName.FirstName() + " at the sight of his "
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and " + part
		sTweet += ".\n\nShe could hardly believe that in a few minutes this man would be " + self.VThrust.Gerund() + " her virgin " + self.FemBodyParts.Vagina.ShortDescription() + "!"
		
		return sTweet
		
class Generator21(Generator):
	#Candy stroked Lorenzo's turgid meat vigorously. Suddenly his engorged head swelled and spurted gobs of white hot semen on her lips, on her breasts, on her thighs, on her pussy. 'Oh God', she said, 'it's all over my nice Easter Sunday outfit!'
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = self.FemaleName.FirstName() + " stroked " + self.MaleName.FirstName() + "'s " + self.MaleBodyParts.Penis.RandomDescription() + " vigorously. Suddenly its " + self.MaleBodyParts.Penis.Head.RandomDescription() + " swelled and he " + self.VEjac.Past() + ", sending gobs of " + self.Semen.RandomDescription() + " all over her "
		
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and her " + part + ".\n\n"
		sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' she said. 'You've ruined my nice " + self.Event.GetWord(bRemoveMy = True) + " dress!'"
		
		return sTweet
		
class Generator22(Generator):
	# John's robe fell to the floor, and Ginger's heart skipped a beat. He had a compact athletic physic with wide shoulders, brawny arms, tight buns, and a 
	# lengthy penis. "I can't believe you're my brother-in-law," she said.	
	def GenerateTweet(self):
		sTweet = ""

		sTweet = self.MaleName.FirstName() + "'s robe fell to the floor, and " + self.FemaleName.FirstName() + "'s heart skipped a beat. He had "
		
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += AddArticles(part) + ", "
			else:
				sTweet += "and " + AddArticles(part) 
		sTweet += ".\n\n'" + self.Exclamation.GetWord().capitalize() + " I can't believe you're my " + self.MFWB.GetPerson() + "!' she said."
		
		return sTweet
		
class Generator23(Generator):
	# 'My mother thinks an opthamolgist and a librarian can never find love together,' said Raoul as Esmerelda lay exhausted in his strong arms.\r\n
	# 'You're no opthamologist,' she replied, panting. 'You're the mayor of Ream My Ass City!'
	def GenerateTweet(self):
		sTweet = ""
		
		sWhiteCollar = self.WhiteCollar.GetPerson()
		sTweet = "'My " + self.FFWB.GetPerson() + " thinks " + AddArticles(sWhiteCollar) + " and his " + self.FFWB.GetPerson() + " can never find love together,' said " + self.MaleName.FirstName() + " as " + self.FemaleName.FirstName() + " lay exhausted in his " + self.MaleBodyParts.Arms.MediumDescription() + ".\n\n"
		sTweet += "'You're no " + sWhiteCollar + ",' she replied, panting. 'You're the mayor of " + self.VThrust.Present().title() + " My " + self.FemBodyParts.GetRandomHole().title() + " City!'"
		
		return sTweet
		
class Generator24(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		
		iRand = randint(1,2)
		iRandGender = randint(1,2)
		
		if iRandGender == 1:
			sHisName = self.MaleName.FirstName()
			sHerName = "the woman"
		else:
			sHisName = "the man"
			sHerName = self.FemaleName.FirstName()
		
		
		self.CreamPieScene = SceneCreamPie(sHerName = sHerName, oLocation = Location)
		
		sTweet = Location.BeginDesc 
		
		if iRand == 2:
			sTweet += " In moments, " + sHisName + " had " + sHerName + " bent over " + Location.BentOver + ", and the two were " + self.VSex.Gerund() + " " + self.VSex.GetAdv() + ".\n\n"
			sTweet += "He was soon " + self.VEjac.Gerund() + " deep within her " + self.FemBodyParts.Ass.Anus.RandomDescription() + " as an intense orgasm wracked her body."
			sTweet += " " + self.CreamPieScene.Scene(bIsVagina = False) + "\n\n" 
		else:
			sTweet += " In moments, " + sHisName + " had " + sHerName + " bent over " + Location.BentOver + ", and the two were " + self.VSex.Gerund() + " " + self.VSex.GetAdv() + ".\n\n"
			sTweet += "He was soon " + self.VEjac.Gerund() + " deep within her " + self.FemBodyParts.Vagina.RandomDescription() + " as an intense orgasm wracked her body."
			sTweet += " " + self.CreamPieScene.Scene() + "\n\n" 
		if iRandGender == 1:
			sTweet += sHisName + " " + Location.PutOnMaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.Punchline.GetPunchline(Gender.Male)
		else: 
			sTweet += sHerName + " " + Location.PutOnFemaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.Punchline.GetPunchline(Gender.Female)
		
		return sTweet
		
class Generator25(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = LocPubPrivType.Public)
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		iRand = randint(1,3)
		
		sTweet = sHerName + " knelt " + Location.KneelingOn + " and " + sHisName + " began to lick her "
		
		if iRand == 1:
			sTweet += self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ". "
		elif iRand == 2:
			sTweet += self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + ". "
		else:
			sTweet += self.FemBodyParts.Ass.Anus.RandomDescription() + ". "
			
		sTweet += "Despite the " + Location.Despite + " it felt amazing. " + sHisName + " eased his " + self.MaleBodyParts.Penis.RandomDescription() + " into her " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + ".\n\n"
		sTweet += "'But " + sHisName + ",' she said, '" + Location.HurryReason + "!'\n\n"
		sTweet += "'Don't worry baby,' he said, " + self.VThrust.Gerund() + " into her.\n\n"
		sTweet += Location.Caught + "\n\n"
		sTweet += "'" + self.Exclamation.GetWord().capitalize() + " I'm gonna cum!' said " + sHisName + ".\n\n"
		sTweet += "'Wait, not yet!' she cried.\n\n"
		sTweet += "'Too late!' said " + sHisName + ". 'I'm " + self.VEjac.Gerund() + "!' And then, " + Location.Consequence + ", he grabbed her by the hips and filled her " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " with " + self.Semen.RandomDescription() + "."
		
		return sTweet
		
class Generator26(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = LocPubPrivType.Public)
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		iRand = randint(1,3)
		iRandLength = randint (7,12)
		
		sTweet = sHisName + " and " + sHerName + " could barely keep their hands off each other as they ripped off their clothes. In moments they were naked in each other's arms. " + sHisName + " squeezed her " + self.FemBodyParts.Ass.RandomDescription() + " as he explored her " + self.FemBodyParts.Mouth.RandomDescription() + " with his tongue.\n\n"
		sTweet += sHerName + " got on her knees and began to " + self.VForeplay.Present() + " his " + str(iRandLength) + "\" " + self.MaleBodyParts.Penis.ShortDescription() + " and " + self.VForeplay.Present() + " his " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + ".\n\n"
		sTweet += "Suddenly, " + sHerName + " froze. " + Location.Caught + "\n\n"
		sTweet += Location.Excuse + "\n\n"
		sTweet += "'" + self.Exclamation.GetWord(bSad = True).capitalize() + "' " + sHerName + " exclaimed. 'I knew it was a bad idea to do this " + Location.NamePrep + "!'"
		
		return sTweet
		
class Generator27(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		sBadGirlName = self.BadGirlName.GetAdj() + " " + self.BadGirlName.GetWord() 
		Location = locations.LocationSelector().Location(PubPrivType = LocPubPrivType.Public)
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "'You're such " + AddArticles(sBadGirlName) + ", " + sHerName + ",' he said.\n\n"
		sTweet += "'I *am* " + AddArticles(sBadGirlName) + ",' she said. 'I'm one for *you*, " + sHisName + ". I'm " + AddArticles(sBadGirlName) + " for your " + self.MaleBodyParts.Penis.RandomDescription() + " in my " + self.FemBodyParts.Mouth.RandomDescription(bAllowLongDesc = False) + ".'\n\n"
		sTweet += "'You're also " + AddArticles(sBadGirlName) + " because you let me " + self.VThrust.Present() + " your " + self.FemBodyParts.Ass.Anus.ShortDescription() + " " + Location.NamePrep + ",' he said."
		
		return sTweet
		
class Generator28(Generator):
	#Doing it in a location. Surprise! They're being watched by her husband.
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		iRand = randint(1,2)
		
		sTweet = Location.BeginDesc
		if not Location.FemaleBottomClothing == "": 
			sTweet += " " + sHisName + " ripped " + sHerName + "'s " + Location.FemaleBottomClothing + " off. "
		sTweet += "She sat down " + Location.SittingOn + " and spread her legs. " + sHisName + " began to "
		if iRand == 1:
			sTweet += self.VForeplay.Present() + " her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + " vigorously.\n\n" 
		else: 
			sTweet += self.VForeplay.Present() + " her " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " tenderly.\n\n"
		sTweet += "'I'm ready!' she " + self.VMoan.Past() + ". 'I want that " + self.MaleBodyParts.Penis.RandomDescription() + " in me right now!'\n\n"
		sTweet += "He inserted his " + self.MaleBodyParts.Penis.ShortDescription() + " into her " + self.FemBodyParts.Vagina.InnerVag.MediumDescription() + " and began to " + self.VThrust.Present() + " it roughly.\n\n"
		sTweet += "'Harder, baby, I want you to " + self.VEjac.Present() + " inside,' she " + self.VMoan.Past() + ". Then she looked over at her husband " + self.MaleName.FirstName() + "."
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet += " 'You like this, baby?' she asked him."
		elif iRand == 2:
			sTweet += " 'Do you want him to do my ass, baby?' she asked him."
		else:
			sTweet += " 'I think he's bigger than you, baby,' she said to him."
		
		return sTweet
		
class Generator29(Generator):
	#Martin walked in to see Sabrina lying on the bed. Her nose was in a book and her short nightgown was hiked up over her pert bottom. Her hand was down her panties and Martin could see that she was frigging her starfish urgently.
	#'What are you reading?' Martin asked.
	#'Sex Slave to the Vampire Pirates,' Sabrina moaned.
	def GenerateTweet(self):
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		iRand = randint(1,2)
		
		sTweet = sHisName + " found " + sHerName + " lying on her bed in her nightgown with her nose in a book and one hand down her lacy panties. She was frigging her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + " with urgent fingers.\n\n"
		sTweet += "'What are you reading?' he asked.\n\n"
		sTweet += "'" + misc.BookTitleBuilder().GetTitle() + ",' " + sHerName + " " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator30(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		iRand = randint(1,2)
		
		sTweet = "'C'mere baby,' she said. 'I want you to suck on my "
		if iRand == 1:
			sTweet += self.FemBodyParts.Breasts.ShortDescription() + ". "
		else:
			sTweet += self.FemBodyParts.Breasts.Nipples.RandomDescription() + ". "
		iRand = randint(1,2)
		if iRand == 1:
			sTweet += "I want to feel your " + self.MaleBodyParts.Penis.RandomDescription() + " against my " + self.FemBodyParts.Ass.ShortDescription() + " "
		else:
			sTweet += "I want you to spread my legs wide and " + self.VForeplay.Present() + " my " + self.FemBodyParts.Vagina.Clitoris.RandomDescription() + " "
		iRand = randint(1,2)
		if iRand == 1:
			sTweet += "and then I want you to " + self.VMakeLove.Present() + " my " + self.FemBodyParts.Vagina.RandomDescription() + ".'\n\n"
		else:
			sTweet += "and then I want you to fill my " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " with your " + self.Semen.RandomDescription() + ".'\n\n"
		
		sTweet += "'Ooooh, yes,' " + self.VMoan.Past() + " " + self.MaleName.FirstName() + ". 'But my priest says it's wrong to do this with my " + self.FFWB.GetPerson() + ".'"
		
		return sTweet
		
class Generator31(Generator):
	# Trevor walked in and froze. His step-sister lay on the bed totally nude. His wide eyes took in her heavy tits, wide hips, sticky folds, and puckered sphincter. The naked guy next to her was idly diddling her peach. He looked up at Trevor. 'You want in?' he asked.
	def GenerateTweet(self):
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sFFWB = self.FFWB.GetPerson()
		
		sTweet = sHisName + " walked in and froze. His " + sFFWB + " lay on the bed totally nude. His wide eyes took in her "
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = True)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and " + part + ".\n\n"
		sTweet += "The naked guy next to her was idly " + self.VForeplay.Gerund() + " her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". He looked up at " + sHisName + ". 'You want in?' he asked."
		
		return sTweet
		
class Generator32(Generator):
	##I've got a present for you, she said. What's that? he asked her. She [bent over and pulled her panties aside, revealing her little starfish.] [lifted up her short skirt revealing that she wasn't wearing any panties. He could clearly see her smooth pussy lips and her inner folds.] [pulled her titties out of her blouse. They were large and gleaming with oil.]
	def GenerateTweet(self):
		sTweet = ""
		
		iRand = randint(1,3)
		
		sTweet = "'I've got a present for you,' she said.\n\n"
		sTweet += "'What's that?' he asked.\n\n"
		if iRand == 1:
			sTweet += "She bent over and pulled her panties aside, revealing her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ".\n\n"
		elif iRand == 2:
			sTweet += "She lifted up her short skirt and he saw that she wasn't wearing panties. Her " + self.FemBodyParts.Vagina.OuterLabia.GetNoun() + " was " + self.FemBodyParts.Vagina.OuterLabia.GetAdj() + " and her " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " peaked out shyly.\n\n"
		else:
			sTweet += "She pulled her " + self.FemBodyParts.Breasts.RandomDescription() + " out of her low-cut blouse. They were large and gleaming with oil.\n\n"
		sTweet += "'Happy " + self.Event.GetWord() + ", baby,' she said."
		
		return sTweet
		
class Generator33(Generator):
	#'I own you now,' he said to the babysitter. "I own your your pretty mouth, I own your lickable tits, I own the dripping folds of your cunt and I even own..." He leaned forward, and whispered in her ear, "Your tight little starfish."
	#"Ooh, yes general," she said.
	def GenerateTweet(self):
		sTweet = ""
		
		sTweet = "'I own you now,' said " + self.MaleName.FirstName() + " to his " + self.FFWB.GetPerson() + ". 'I own your " + self.FemBodyParts.Lips.RandomDescription() + ", I own your " + self.FemBodyParts.Breasts.RandomDescription() + ", I own the " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " of your " + self.FemBodyParts.Vagina.ShortDescription() + ", and I even own...' He leaned in and whispered in her ear, 'Your " + self.FemBodyParts.Ass.Anus.RandomDescription() + ".'\n\n"
		sTweet += "'Ooh, yes sir!' she " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator34(Generator):
	#'It was just a silly bet,' he said.\n\n
	#'No, fair is fair,' she said, pulling down her panties. 'I said that you could use my cocksock any way you want, right here in the woods, and I never go back on a bet.' 
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = LocPubPrivType.Public)
		iRand = randint(1,4)
		
		sTweet = "'It was just a silly bet,' " + self.MaleName.FirstName () + " said to his " + misc.WomanAdjs().GetWord() + " " + self.FFWB.GetPerson() + ". 'Don't worry about it.'\n\n"
		sTweet += "'No, fair is fair,' " + self.FemaleName.FirstName() + " said, pulling down her " + Location.FemaleBottomClothing + ". "
		if iRand == 1:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Vagina.RandomDescription() + " any way you want, "
		elif iRand == 2:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " any way you want, "
		elif iRand == 3:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Ass.RandomDescription() + " any way you want, "
		else:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Ass.Anus.RandomDescription() + " any way you want, "
		sTweet += "right here " + Location.NamePrep + ", and I never go back on a bet.' "
		
		return sTweet
		
class Generator35(Generator):
		#'Oh baby,' she said. 'I love you so much. I just want to be with you and make you happy. Tell me what I can do,' she said, giving him a peck on the lips.
		#'I want {to fuck your big titties / to put my finger in your butthole / to put my balls in your mouth / you to eat out my starfish },' he said.
	def GenerateTweet(self):
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = LocPubPrivType.Private)
		
		iRand = randint(1,4)
		sHisName = self.MaleName.FirstName()
		
		sTweet = "'Oh " + sHisName + ",' " + self.FemaleName.FirstName() + " said to him. They were sitting together " + Location.NamePrep + ". 'I love you so much. I just want to be with you and make you happy. Just tell me how,' she said, giving him a peck on the lips.\n\n"
		if iRand == 1:
			sTweet += "'I want to rub my " + self.MaleBodyParts.Penis.ShortDescription() + " on your " + self.FemBodyParts.Breasts.RandomDescription(bAllowLongDesc = False) + "', he said."
		elif iRand == 2:
			sTweet += "'I want to put my finger in your " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' he said."
		elif iRand == 3:
			sTweet += "'I want to put my " + self.MaleBodyParts.Penis.Testicles.ShortDescription() + " in your mouth,' he said."
		else:
			sTweet += "'I want you to eat out my " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' he said."
		
		return sTweet
		
class Generator36(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator37(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator38(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator39(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator40(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator41(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator42(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator43(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator44(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator45(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator46(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator47(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class Generator48(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		
		
		return sTweet
		
class GeneratorPromo(Generator):
	def GenerateTweet(self):
		sTweet = ""
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet = misc.TweetReplyBuilder().GetReply() + " from Flaming Lust Bot!"
		elif iRand == 2:
			sTweet = misc.TweetReplyBuilder().GetReply() + " from Flaming Lust Bot!"
		else:
			sTweet = "Filthy Lust Bot is a twitter bot designed to automatically generate erotic love scenes and tweet them out. Sometimes they're hot, or filthy, or funny. Like and RT if you enjoy!\n\nTweets for those 18+ only! 🔞\n\nReply to @bot_lust and it will plug a (made up) book!"
			
		return sTweet