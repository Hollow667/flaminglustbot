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
	sTweet = ""
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if not gen == None:
			sTweet = gen.GenerateTweet()
	else:
		gen = GenSel.RandomGenerator()
		while gen.ID in HistoryQ:
			gen = GenSel.RandomGenerator()
		if not gen == None:
			sTweet = gen.GenerateTweet()
			
			HistoryQ.insert(0, gen.ID)
			
			if len(HistoryQ) > Q_SIZE:
				HistoryQ.pop()
		
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
	
	#print("Prefix is [" + sPrefix + "]")
	sTweetStr = GetTweet(bTest, iGeneratorNo)
	#print(sTweetStr)
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
	ID = -1
	Priority = 1
	
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
	
	def GenerateTweet(self):
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
	
		return ""
		
class GeneratorPromo(Generator):
	ID = 0
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iRand = randint(1,6)
		if iRand == 1:
			sTweet = misc.TweetReplyBuilder().GetReply() + " from Flaming Lust Bot!"
		elif iRand == 2:
			sTweet = "Reply to a Flaming Lust Bot tweet with a tweet containing '#book' and it will tweet a random smutty book title at you! Use '#lovescene' instead to get your own custom filthy love scene!"
		elif iRand == 3:
			sTweet = "Tell your family, friends and lovers to follow @bot_lust for all the steamy, sweaty, silly action!😘"
		elif iRand == 4:
			sTweet = "Flaming Lust Bot is very naughty, and NOT appropriate for anyone under 18!🔞\n\nThat includes you, kid who is hiding their phone behind their math book while they check twitter!!!"
		elif iRand == 5:
			sTweet = "Flaming Lust Bot is a twitter bot designed to automatically generate erotic love scenes and tweet them out. Tweets might be hot, or filthy, or funny. Like and RT if you enjoy!\n\nTweets for those 18+ only! 🔞\n\nReply to @bot_lust and get a surprise!"
		else:
			sTweet = "I love you, followers!\n\n💚💙💜"
			
		return sTweet
		
class Generator1(Generator):
	ID = 1
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		# The baron desecrated Jacinda's well-used muffin with his thick pole.	
		sVerb = self.VForeplay.Present()
		sTweet = "The " + self.WealthyMan.GetPerson() + " " + self.VThrust.Past() + " " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n'" + sVerb.capitalize() + " my " + self.FemBodyParts.Breasts.RandomDescription() + "!' she " + self.VMoan.Past() + ". '" + sVerb.capitalize() + " them and fill me with your " + self.Semen.FloweryDescription() + "!'"
		
		return sTweet
		
class Generator2(Generator):
	# Spreading open her supple buttocks with his rough hands, he desecrated her well-used anus with his erect boner. 'Fuck me,
	# Jordan!' she screamed. 'Pound me like your wife!'	
		
	ID = 2
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 3
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'Please, no!' " + self.FemaleName.FirstName() + " " + self.VMoan.Past() + ", squirming with pleasure as " + self.MaleName.FirstName() + " " + self.VThrust.Past() + " her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". 'Not while my " + self.MFWB.GetPerson() +" is watching!'"
		
		return sTweet

class Generator4(Generator):
	# 'You may cum inside my womanhood if you like', she instructed him, 'But only my photographer is allowed to bayonette my sphincter.'	
	ID = 4
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'You may cum inside my " + self.FemBodyParts.Vagina.ShortDescription() + " if you like', " + self.FemaleName.FirstName() + " instructed him, 'But only my " + self.MFWB.GetPerson() + " is allowed to " + self.VThrust.Present() + " my " + self.FemBodyParts.Ass.Anus.RandomDescription() + "'."
		
		return sTweet
		
class Generator5(Generator):
	# 'Oh, Leon,' she moaned, 'I'm so thirsty for your glossy spunk!' 'But Ophelia,' he said, 'You're my mother-in-law!'
	ID = 5
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'Oh, " + self.MaleName.FirstName() + ",' she " + self.VMoan.Past() + " in his " + self.MaleBodyParts.Arms.MediumDescription() + ", 'I'm so thirsty for your " + self.Semen.RandomDescription() + "!'\n\n'But " + self.FemaleName.FirstName() + ",' he said, 'You're my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
class Generator6(Generator):
	# 'You don't have to hide the truth from me, Honey,' he said, 'Tom is a successful opthamologist and I'm just a lowly roadie!' 
	# 'That's true,' she said, 'But YOU have a 8 1/2 inch fuck-pole!'	
	ID = 6
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sRivalName = self.MaleName.FirstName()
		sTweet = "'You don't have to hide the truth from me, " + self.FemaleName.FirstName() + ",' he said, '" + sRivalName + " is a successful " + self.WhiteCollar.GetPerson() + " and I'm just a lowly " + self.BlueCollar.GetPerson() + "!'\n\n'I don't care about " + sRivalName + ",' she said, 'You're the one I want. And anyway, you have a " + str(randint(8, 12)) + " 1/2 inch " + self.MaleBodyParts.Penis.ShortDescription() + "!'"
		
		return sTweet
		
class Generator7(Generator):
	# Charity bit her lip as Tristan fondled her heaving bosoms. 'Oh god,' she said, 'What would my pastor say if he saw that I was letting my pool boy pump into my crack?'	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		
		sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on " + Location.LyingOn + ", her " + self.FemBodyParts.Breasts.RandomDescription() + " heaving as " + self.MaleName.FirstName() + " lubed up her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ". '" + self.Exclamation.GetWord().capitalize() + "' she " + self.VMoan.Past() + ", 'What would Father " + self.MaleName.FirstName() + " say if he knew that my " + self.MFWB.GetPerson() + " was " + self.VThrust.Gerund() + " my " + self.FemBodyParts.Ass.ShortDescription() + " " + Location.NamePrep + "?'"
		
		return sTweet

class Generator8(Generator):
	#Bianca bit her lip as he caressed her youthful thighs. 'Ferdinand!' she said, 'My urologist is in the next room!' 
	#'Should we invite him?' he asked innocently, inserting a finger into her love channel.	
	ID = 8
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(InOut = LocInOutType.Indoors)
		
		sBoyfriendName = self.MaleName.FirstName()
		sTweet = self.FemaleName.FirstName() + " bit her lip as he " + self.VForeplay.Past() + " her " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " " + Location.NamePrep + ". "
		sTweet += "'" + sBoyfriendName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson() + " is right outside!'\n\n'Do you think he'd like to join us?' " + sBoyfriendName + " asked innocently, inserting a finger into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
		
		return sTweet
		
class Generator9(Generator):
	# 'What?' she said. 'Hasn't a girl ever let you fuck her oiled-up coconuts with your meat pole before?''Only my dad's girlfriend,' he replied.
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'What?' she asked. 'Hasn't a girl ever let you fuck her big, oiled-up " + self.FemBodyParts.Breasts.ShortDescription() + " with your " + self.MaleBodyParts.Penis.RandomDescription() + " before?'\n\n'Only my " + self.FFWB.GetPerson() + ",' " + self.MaleName.FirstName() + " replied."
		
		return sTweet
		
class Generator10(Generator):
	#'Oh lord, what a day it has been,' said the dutchess. Ripping open her blouse, she exposed her massive double-D mammaries. 'Come, my little fry cook, I need you to nibble on my buns and then to cover my hard nipples in your salty man jam.'
	ID = 10
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "'" + self.Exclamation.GetWord(bExMk = False).capitalize() + ", what a day it has been,' said the " + misc.WomanAdjs().GetWord() + " " + self.WealthyWoman.GetPerson() +". Ripping open her blouse, she exposed her " + self.FemBodyParts.Breasts.RandomDescription() + " to him. 'Come, my little " + self.BlueCollar.GetPerson() + ". I need you to " + self.VForeplay.Present() + " my " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " and cover my " + self.FemBodyParts.GetRandomBodyParts(1, False, True)[0] + " in your "+ self.Semen.RandomDescription() + ".'"
		
		return sTweet
		
class Generator11(Generator):
	# 'Oh God, Julia,' he said, 'You are so beautiful. I love your supple skin, your sumptuous hips, your perfect thighs, the way
	# you look with my ballsack in your mouth.'
	ID = 11
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'" + self.Exclamation.GetWord(bExMk = False, bHappy = True).capitalize() + ", " + self.FemaleName.FirstName() + ",' he " + self.VMoan.Past() + ", 'You are so beautiful. I love your "
		for part in self.FemBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False):
			sTweet += part + ", "
		sTweet += "and the way you look with my " + self.MaleBodyParts.Penis.GetRandomPenisPart() + " in your " + self.FemBodyParts.Mouth.RandomDescription() + ".'"
		
		return sTweet
		
class Generator12(Generator):
	# Ginger's robe fell to the floor, and his heart skipped a beat. She had a shapely form with ripe boobs, wide hips, and a 
	# well-used hole. "I can't believe you're my sister," he said.	
	ID = 12
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 13
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 14
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'Oh " +self.MaleName.FirstName() + ",' she said, 'I've never been with a " + self.WealthyMan.GetPerson() + " before.'\n\n"
		sTweet += "'Fear not, my darling love, I would never hurt you,' he said as he began to " + self.VMakeLove.Present() + " her " + self.FemBodyParts.GetRandomHole() + " with his " + str(randint(8,14)) + "\" " + self.MaleBodyParts.Penis.RandomDescription() + "."
		
		return sTweet
		
class Generator15(Generator):
	# 'Vance, my love, where are you?' called Anjelica from the next room. Vance looked down at Veronica. Her dazzling blue eyes 
	# were locked on his as she wrapped her hungry mouth around his massive meat pole. "I'll just be a minute dear," Vance replied.
	ID = 15
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iRand = randint(1,3)
				
		sBoyfriendName = self.MaleName.FirstName()
		sTweet = "'" + sBoyfriendName + ", my love, where are you?' called " + self.FemaleName.FirstName() + " from the next room.\r\n"
		sTweet += sBoyfriendName + " looked down at " + self.FemaleName.FirstName() + ". "
		if iRand == 1:
			sTweet += "Her head was cupped in his hands as she bobbed up and down on his " + self.MaleBodyParts.Penis.FloweryDescription() + ".\n\n"
		elif iRand == 2:
			iRandCockLen = randint(6,10)
			sTweet += "Tears trailed from her " + self.FemBodyParts.Eyes.RandomDescription() + " as she took his " + str(iRandCockLen) + "\" " + self.MaleBodyParts.Penis.FloweryDescription() + " deep into her throat.\n\n"
		elif iRand == 3:
			iRandCockLen = randint(6,10)
			sTweet += "Her " + self.FemBodyParts.Lips.GetAdj() + " lips were wrapped around his " + self.MaleBodyParts.Penis.Head.RandomDescription(bAllowShortDesc = True) + " and she was gently massaging his " + self.MaleBodyParts.Penis.Testicles.ShortDescription() + ".\n\n"
		else:
			sTweet += "Her " + self.FemBodyParts.Eyes.RandomDescription() + " were locked on his as she wrapped her " + self.FemBodyParts.Mouth.RandomDescription() + " around his " + self.MaleBodyParts.Penis.FloweryDescription() + ".\n\n"
		sTweet += "'I'll just be a minute dear,' " + sBoyfriendName + " replied."
		
		return sTweet
		
class Generator16(Generator):
	# Devon squeezed and sucked on Sabrina's luscious double-D mammaries as he fingered her clit and jackhammered her willing cunt 
	# hole. 'My god,' whispered Grant, stroking his meat sword, 'I can't believe I'm watching my wife fuck an opthamologist!'"
		
	ID = 16
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.MaleName.FirstName() + " squeezed and sucked on " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.Breasts.RandomDescription() + " as he fingered her " + self.FemBodyParts.Vagina.Clitoris.RandomDescription() + " and " + self.VThrust.Past() + " her " + self.FemBodyParts.GetRandomHole() + ".\n\n"
		sTweet += "'" + self.Exclamation.GetWord(bHappy = True).capitalize() + "' " + self.VMoan.Past() + " " + self.MaleName.FirstName() + ", stroking his " + self.MaleBodyParts.Penis.RandomDescription() + " as he looked on, 'I can't believe I'm watching my wife " + self.VSex.Present() + " " + AddArticles(self.WhiteCollar.GetPerson()) + "!'"
		
		return sTweet
		
class Generator17(Generator):
	# Charity's eyes were wide as she cupped his dangling nutsack. 'Does every opthamologist have one like this?' she asked. 
	# 'No darling,' said Brad. 'Not every opthamologist has a 9 1/2 inch meat sword. Now play with my testicles while you rub the swollen head.'
	ID = 17
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sWhiteCollarJob = self.WhiteCollar.GetPerson()
		sTweet = self.FemaleName.FirstName() + " stared with innocent " + self.FemBodyParts.Eyes.MediumDescription() + " at his " + self.MaleBodyParts.Penis.MediumDescription() + ". 'Does every " + sWhiteCollarJob + " have a... thing like this?' she asked.\n\n"
		sTweet += "'No darling,' said " + self.MaleName.FirstName() + " chuckling. 'Not every " + sWhiteCollarJob + " has a " + str(randint(8, 12)) + "\" " + self.MaleBodyParts.Penis.ShortDescription() + ". Now massage my " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + " while you suck on my " + self.MaleBodyParts.Penis.Head.ShortDescription() + ".'"
		
		return sTweet
		
class Generator18(Generator):
	# "'Jacinda, my dear, I wrote you a poem,' he said. 'What is it about?' asked Jacinda. 'It's about you, my love: your golden 
	# hair, your generous tits, your smooth legs, your dangling labia.' 'Oh Brad!' she sighed."
	ID = 18
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 20
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = self.MaleName.FirstName() + " approached the bed completely naked. A thrill ran through " + self.FemaleName.FirstName() + " at the sight of his "
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and " + part
		sTweet += ".\n\nShe could hardly believe that in a few minutes this man would be " + self.VThrust.Gerund() + " her virgin " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + "!"
		
		return sTweet
		
class Generator21(Generator):
	#Candy stroked Lorenzo's turgid meat vigorously. Suddenly his engorged head swelled and spurted gobs of white hot semen on her lips, on her breasts, on her thighs, on her pussy. 'Oh God', she said, 'it's all over my nice Easter Sunday outfit!'
	ID = 21
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 22
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 23
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sWhiteCollar = self.WhiteCollar.GetPerson()
		sTweet = "'My " + self.FFWB.GetPerson() + " thinks " + AddArticles(sWhiteCollar) + " and his " + self.FFWB.GetPerson() + " can never find love together,' said " + self.MaleName.FirstName() + " as " + self.FemaleName.FirstName() + " lay exhausted in his " + self.MaleBodyParts.Arms.MediumDescription() + ".\n\n"
		sTweet += "'You're no " + sWhiteCollar + ",' she replied, panting. 'You're the mayor of " + self.VThrust.Present().title() + " My " + self.FemBodyParts.GetRandomHole(bAllowShortDesc = True).title() + " City!'"
		
		return sTweet
		
class Generator24(Generator):
	ID = 24
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
		
		
		CreamPieScene = SceneCreamPie(sHerName = sHerName, oLocation = Location)
		
		sTweet = Location.BeginDesc 
		
		if iRand == 2:
			sTweet += " In moments, " + sHisName + " had " + sHerName + " bent over " + Location.BentOver + ", and the two were " + self.VSex.Gerund() + " " + self.VSex.GetAdv() + ".\n\n"
			sTweet += "He was soon " + self.VEjac.Gerund() + " deep within her " + self.FemBodyParts.Ass.Anus.RandomDescription() + " as an intense orgasm wracked her body."
			sTweet += " " + CreamPieScene.Scene(bIsVagina = False) + "\n\n" 
		else:
			sTweet += " In moments, " + sHisName + " had " + sHerName + " bent over " + Location.BentOver + ", and the two were " + self.VSex.Gerund() + " " + self.VSex.GetAdv() + ".\n\n"
			sTweet += "He was soon " + self.VEjac.Gerund() + " deep within her " + self.FemBodyParts.Vagina.RandomDescription() + " as an intense orgasm wracked her body."
			sTweet += " " + CreamPieScene.Scene() + "\n\n" 
		if iRandGender == 1:
			sTweet += sHisName + " " + Location.PutOnMaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.Punchline.GetPunchline(Gender.Male)
		else: 
			sTweet += sHerName + " " + Location.PutOnFemaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.Punchline.GetPunchline(Gender.Female)
		
		return sTweet
		
class Generator25(Generator):
	ID = 25
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	#Naked in a public location and cuaght.
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	# 'You're such a slut, Veronica,' he said. 'I *am* a slut,' she said. 'I'm one for *you*, James. I'm a slut for your hard cock in my mouth.' 'You're also a slut because you let me fuck your backdoor in the bathroom at Starbucks,' he said.
	ID = 27
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 28
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		iRand = randint(1,2)
		
		sTweet = Location.BeginDesc + " "
		if not Location.FemaleBottomClothing == "": 
			sTweet += sHisName + " ripped " + sHerName + "'s " + Location.FemaleBottomClothing + " off. "
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
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		iRand = randint(1,2)
		
		sTweet = sHisName + " found " + sHerName + " lying on her bed in her nightgown with her nose in a book and one hand down her lacy panties. She was frigging her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + " with urgent fingers.\n\n"
		sTweet += "'What are you reading?' he asked.\n\n"
		sTweet += "'" + misc.BookTitleBuilder().GetTitle() + ",' " + sHerName + " " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator30(Generator):
	ID = 30
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 31
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 32
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 33
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'I own you now,' said " + self.MaleName.FirstName() + " to his " + self.FFWB.GetPerson() + ". 'I own your " + self.FemBodyParts.Lips.RandomDescription() + ", I own your " + self.FemBodyParts.Breasts.RandomDescription() + ", I own the " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " of your " + self.FemBodyParts.Vagina.ShortDescription() + ", and I even own...' He leaned in and whispered in her ear, 'Your " + self.FemBodyParts.Ass.Anus.RandomDescription() + ".'\n\n"
		sTweet += "'Ooh, yes sir!' she " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator34(Generator):
	#'It was just a silly bet,' he said.\n\n
	#'No, fair is fair,' she said, pulling down her panties. 'I said that you could use my cocksock any way you want, right here in the woods, and I never go back on a bet.' 
	ID = 34
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	ID = 35
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
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
	#Their masked host guided them into the banquet hall. On the dining table a beautiful woman lay spread-eagled, completely naked, in the center. Her succulent bronzed skin was dripping with honey, her lissome form was covered with fruits and berries, her navel was brimming with liquor, her full, perfect breasts were topped with whipped cream, and her pussy was stuffed with a single ripe strawberry. 'Gentlemen,' said the marquis, 'Let's eat!'\n\n'Holy fuck,' thought Leon, 'That's my step-daughter!'
	ID = 36
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		print("Generator36 active")
		
		sTweet = "Their masked host ushered them into the banquet hall. In the center of the dining table a beautiful woman lay spread-eagled, completely naked. "
		
		Feast = []
		Feast.append("her succulent " + self.FemBodyParts.Skin.GetAdj(sNot = "succulent") + " " + self.FemBodyParts.Skin.GetNoun() + " was dripping with syrup") 
		#print("Added syrup")
		Feast.append("she held a ripe cherry between her " + self.FemBodyParts.Lips.GetAdj(sNot = "cherry") + " lips")
		#print("Added cherry")
		Feast.append("her " + self.FemBodyParts.GetAdj(sNot = "womanly") + " " + self.FemBodyParts.GetNoun() + " was covered with fruits and berries")
		#print("Added fruit")
		Feast.append("her navel was a goblet brimming with liquor") 
		#print("Added liquor")
		Feast.append("her full, " + self.FemBodyParts.Breasts.GetAdj(sNot = "full") + " " + self.FemBodyParts.Breasts.GetNoun() + " were topped with whip cream")
		#print("Added whip cream")
		Feast.append("the inside of her " + self.FemBodyParts.Thighs.ShortDescription() + " were glazed with chocolate")
		#print("Added chocolate sauce")
		Feast.append("her " + self.FemBodyParts.Vagina.OuterLabia.GetNoun() + " gleamed with sticky honey")
		#print("Added honey")
			
		sFeast = ""
		if len(Feast) > 0:
			for x in sorted(sample(range(0, len(Feast)), 3)): 
				sFeast += Feast[x] + ", "
			sFeast += "and a "
			sFeast = sFeast.capitalize()
		else: 
			sFeast = "A "
				
		sTweet += sFeast + "single, ripe strawberry was stuffed in her " + self.FemBodyParts.Vagina.MediumDescription() + ". "
		sTweet += "'Gentlemen,' said the " + self.WealthyMan.GetPerson() + ", 'Let's feast!'\n\n"
		sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' thought " + self.MaleName.FirstName() + ", 'That's my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
# class Generator37(Generator):
	# ID = 37
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# sHisName = self.MaleName.FirstName()
		# sHerName = self.FemaleName.FirstName()
		
		# Location = locations.LocationSelector().Location()
		# AnalScene = SceneAnal(sHisName = sHisName, sHerName = sHerName, oLocation = Location)
		
		# sTweet = Location.BeginDesc + " "
		
		# sTweet += AnalScene.Scene()
		# sTweet += "\n\n" + AnalScene.ShortScene()
		
		# return sTweet
		
class Generator38(Generator):
	# Husband gets a surprise birthday present from his wife
	ID = 38
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ThirdAdj = WordList(['blonde', 'redheaded', 'brunette', 'Asian', 'black'])
		
		sGiverName = ""
		sBirthdayName = ""
		
		if CoinFlip():
			sGiverName = self.FemaleName.FirstName()
			sBirthdayName = self.MaleName.FirstName()
		
			sTweet = sBirthdayName + " entered the bedroom. " + sGiverName + " was lying on the bed stark naked. His gaze lingered on her "
			
			Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
			for part in Parts:
				if not part == Parts[len(Parts) - 1]:
					sTweet += part + ", "
				else:
					sTweet += "and " + part
			sTweet += ". 'This is a great birthday present, babe,' he said.\n\n"
			sTweet += "'This isn't your present,' said " + sGiverName + "."
			
		else:
			sGiverName = self.MaleName.FirstName()
			sBirthdayName = self.FemaleName.FirstName()
		
			sTweet = sBirthdayName + " entered the bedroom. " + sGiverName + " was wearing nothing but a cowboy hat and his " + self.MaleBodyParts.RandomDescription() + " gleamed with oil. Her gazed lingered on his "
			
			Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
			for part in Parts:
				if not part == Parts[len(Parts) - 1]:
					sTweet += part + ", "
				else:
					sTweet += "and " + part
			sTweet += ". 'This is a great birthday present, babe,' she said.\n\n"
			sTweet += "'This isn't your present,' said " + sGiverName + "."
			
		if CoinFlip():
			sTweet += " A tall " + ThirdAdj.GetWord() + " woman stepped thru the bathroom door. She opened her robe to reveal her naked body. Her sumptuous " + self.FemBodyParts.Breasts.GetNoun(sNot = "sumptuous") + " were full and heavy and her " + self.FemBodyParts.Vagina.GetNoun() + " was shaved bare.\n\n"
		else:
			sTweet += " A tall " + ThirdAdj.GetWord() + " man stepped thru the bathroom door. He opened his robe to reveal his naked body. His strapping chest was " + self.MaleBodyParts.Chest.GetAdj(sNot = "strapping") + " and his " + self.MaleBodyParts.Penis.GetNoun() + " was " + self.MaleBodyParts.Penis.GetAdj() + " and " + self.MaleBodyParts.Penis.GetAdj() + ".\n\n"
			
		sTweet += "'THIS is your birthday present,' " + sGiverName + " said."
		
		return sTweet
		
# class Generator39(Generator):
	# ID = 39
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator40(Generator):
	# ID = 40
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator41(Generator):
	# ID = 40
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator42(Generator):
	# ID = 40
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator43(Generator):
	# ID = 43
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator44(Generator):
	# ID = 44
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator45(Generator):
	# ID = 45
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator46(Generator):
	# ID = 46
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator47(Generator):
	# ID = 47
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator48(Generator):
	# ID = 48
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet

# class Generator49(Generator):
	# ID = 49
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		
		
		# return sTweet
		
# class Generator50(Generator):
	# ID = 50
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
				
class GeneratorSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in Generator.__subclasses__():
			item = subclass()
			for x in range(0, item.Priority):
				self.GeneratorList.append([item.ID, item])
			
	def RandomGenerator(self):
		Generator = None
		
		if len(self.GeneratorList) > 0:
			iRand = randint(0, len(self.GeneratorList) - 1)
			Generator = self.GeneratorList[iRand][1]
			
		return Generator 
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		