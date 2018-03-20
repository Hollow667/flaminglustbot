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
	PresentList = ['make love to',
		'ease into',
		'enter',
		'push into',
		'sex']
		
	PastList = ['made love to',
		'eased into',
		'entered',
		'pushed into',
		'sexed']
		
	GerundList = ['making love to',
		'easing into',
		'entering',
		'pushing into',
		'sexing']
		
	def __init__(self):
		Harder = VerbThrust()
		
		for PresentVerb in Harder.PresentList:
			self.PresentList.append("gently " + PresentVerb)
			self.PresentList.append("lovingly " + PresentVerb)
			self.PresentList.append("carefully " + PresentVerb)
			
		for PastVerb in Harder.PastList:
			self.PastList.append("gently " + PastVerb)
			self.PastList.append("lovingly " + PastVerb)
			self.PastList.append("carefully " + PastVerb)
			
		for Gerund in Harder.GerundList:
			self.GerundList.append("gently " + Gerund)
			self.GerundList.append("lovingly " + Gerund)
			self.GerundList.append("carefully " + Gerund)
		
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