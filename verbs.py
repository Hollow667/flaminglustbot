# Verbs module

from random import *
import util

class Verb:
	PastList = []
	PresentList = []
	GerundList = []
	AdverbList = []
	
	def Past(self):
		sPastVerb = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.PastList) - 1)
		
		sPastVerb = self.PastList[iRandIndex]
		
		return sPastVerb
		
	def Present(self):
		sPresentVerb = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.PresentList) - 1)
		
		sPresentVerb = self.PresentList[iRandIndex]
		
		return sPresentVerb
		
	def Gerund(self):
		sGerundVerb = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.GerundList) - 1)
		
		sGerundVerb = self.GerundList[iRandIndex]
		
		return sGerundVerb
		
	def GetAdv(self):
		sAdverb = ""
		
		if not self.AdverbList == None and len(self.AdverbList) > 0:
			iRand = randint(0, len(self.AdverbList) - 1)
			sAdverb = self.AdverbList[iRand]
			
		return sAdverb
		
class VerbThrust(Verb):
	PresentList = ['bang',
		'bore into',
		'burrow into',
		'delve into',
		'desecrate',
		'defile',
		'do',
		'drill',
		'fill',
		'fuck',
		'hammer',
		'impale',
		'jackhammer',
		'nail',
		'penetrate',
		'piston into',
		'plough',
		'pound',
		'probe',
		'pump into',
		'ram',
		'ravage',
		'ravish',
		'ream',
		'rut in',
		'slam',
		'stuff',
		'thrust into',
		'violate']
		
	PastList = ['banged',
		'bored into',
		'burrowed into',
		'delved into',
		'desecrated',
		'defiled',
		'did',
		'drilled',
		'eagerly filled',
		'fucked',
		'hammered',
		'impaled',
		'jackhammered',
		'nailed',
		'penetrated',
		'pistoned into',
		'ploughed',
		'pounded',
		'probed',
		'pumped into',
		'rammed relentlessly into',
		'ravaged',
		'ravished',
		'reamed',
		'rutted in',
		'slammed into',
		'stuffed',
		'thrust deep into',
		'violated']
		
	GerundList = ['banging',
		'boring into',
		'burrowing into',
		'delving into',
		'desecrating',
		'defiling',
		'doing',
		'drilling',
		'eagerly filling',
		'fucking',
		'hammering',
		'impaling',
		'jackhammering',
		'nailing',
		'penetrating',
		'pistoning into',
		'ploughing',
		'pounding',
		'probing',
		'pumping into',
		'ramming relentlessly into',
		'ravaging',
		'ravishing',
		'reaming',
		'rutting in',
		'slamming into',
		'stuffing',
		'thrusting deep into',
		'violating']
		
class VerbMakeLove(Verb):
	PresentList = []
	PastList = []
	GerundList = []
		
	def __init__(self):
		self.PresentList = ['make love to',
			'ease into',
			'enter',
			'push into',
			'sex']
		
		self.PastList = ['made love to',
			'eased into',
			'entered',
			'pushed into',
			'sexed']
		
		self.GerundList = ['making love to',
			'easing into',
			'entering',
			'pushing into',
			'sexing']
		Harder = VerbThrust()
		
		Prefixes = util.WordList(['gently','lovingly','carefully','tenderly'])
		
		iNumAdd = len(self.PresentList)
		#print("len(self.PresentList) = " + str(iNumAdd))
		for x in sample(range(0, len(Harder.PresentList)), iNumAdd):
			#print("len(Harder.PresentList) = " + str(len(Harder.PresentList)) + ", x = " + str(x))
			self.PresentList.append(Prefixes.GetWord() + " " + Harder.PresentList[x])
			
		iNumAdd = len(self.PastList)
		#print("len(self.PastList) = " + str(iNumAdd))
		for x in sample(range(0, len(Harder.PastList)), iNumAdd):
			#print("len(Harder.PastList) = " + str(len(Harder.PastList)) + ", x = " + str(x))
			self.PastList.append(Prefixes.GetWord() + " " + Harder.PastList[x])
			
		iNumAdd = len(self.GerundList)
		#print("len(self.GerundList) = " + str(iNumAdd))
		for x in sample(range(0, len(Harder.GerundList)), iNumAdd):
			#print("len(Harder.GerundList) = " + str(len(Harder.GerundList)) + ", x = " + str(x))
			self.GerundList.append(Prefixes.GetWord() + " " + Harder.GerundList[x])
		
class VerbEjaculate(Verb):
	PresentList = ['burst',
		'climax',
		'cum',
		'cum hard',
		'ejaculate',
		'erupt',
		'explode',
		'gush',
		'jizz',
		'orgasm',
		'nut',
		'spurt',
		'squirt']
		
	PastList = ['burst',
		'climaxed',
		'came',
		'came hard',
		'ejaculated',
		'erupted',
		'exploded',
		'gushed',
		'jizzed',
		'nutted',
		'orgasmed',
		'spurted',
		'squirted']
		
	GerundList = ['bursting',
		'climaxing',
		'cumming',
		'cumming hard',
		'ejaculating',
		'erupting',
		'exploding',
		'gushing',
		'jizzing',
		'nutting',
		'orgasming',
		'spurting',
		'squirting']
		
class VerbForeplay(Verb):
	PresentList = ['caress',
		'finger',
		'fondle',
		'kiss',
		'lick',
		'nibble on',
		'play with',
		'rub',
		'rub',
		'squeeze',
		'stroke',
		'suck',
		'tease']
		
	PastList = ['caressed',
		'fingered',
		'fondled',
		'kissed',
		'licked',
		'nibbled on',
		'played with',
		'rubbed',
		'squeezed',
		'stroked',
		'sucked',
		'teased']
		
	GerundList = ['caressing',
		'fingering',
		'fondling',
		'kissing',
		'licking',
		'nibbling on',
		'playing with',
		'rubbing',
		'squeezing',
		'stroking',
		'sucking',
		'teasing']
		
class VerbSex(Verb):
	PresentList = ['bang',
		'boink',
		'fuck',
		'go at it',
		'have sex',
		'hump',
		'make love']
		
	PastList = ['banged',
		'boinked',
		'fucked',
		'went at it',
		'had sex',
		'humped',
		'made love']
		
	GerundList = ['banging',
		'boinking',
		'fucking',
		'going at it',
		'having sex',
		'humping',
		'making love']
		
	AdverbList = ['ardently',
		'enthusiastically',
		'fervently',
		'fervidly',
		'feverishly',
		'heedlessly',
		'intensely',
		'passionately',
		'rapturously']
		
class VerbMoan(Verb):
	PresentList = ['cry',
					'gasp',
					'groan',
					'moan',
					'murmur',
					'pant',
					'purr',
					'says',
					'scream',
					'sigh',
					'wail',
					'whimper',
					'whisper']
				
	PastList = ['cried',
				'gasped',
				'groaned',
				'moaned',
				'murmured',
				'panted',
				'purred',
				'said',
				'screamed',
				'sighed',
				'wailed',
				'whimpered',
				'whispered']
	
	GerundList = ['crying',
					'gasping',
					'groaning',
					'moaning',
					'murmuring',
					'panting',
					'purring',
					'saying',
					'screaming',
					'sighing',
					'wailing',
					'whimpering',
					'whispering',]