# Body Parts module

from random import *
import util 


class BodyParts:
	NounList = []
	AdjList = []
	DefaultNoun = ""
	DefaultAdj = "naked"
	IsPlural = True
	
	def GetNoun(self):
		sNoun = ""
		
		if len(self.NounList) > 0:
			iNounIndex = randint(0, len(self.NounList) - 1)
			sNoun = self.NounList[iNounIndex]
			
		return sNoun
	
	def GetAdj(self):
		sAdj = ""
		
		if len(self.AdjList) > 0:
			iAdjIndex = randint(0, len(self.AdjList) - 1)
			sAdj = self.AdjList[iAdjIndex]
			
		return sAdj

	def ShortDescription(self):
		return self.GetNoun()
	
	def MediumDescription(self):
		sMediumDesc = ""
		
		if len(self.NounList) > 0 and len(self.AdjList) > 0:
			iNounIndex = randint(0, len(self.NounList) - 1)
			iAdjIndex = randint(0, len(self.AdjList) - 1)
			
			sMediumDesc = self.AdjList[iAdjIndex] + " " + self.NounList[iNounIndex]
		else:
			sMediumDesc = ""
			
		return sMediumDesc
	
	def FloweryDescription(self):
		sFloweryDesc = ""
		
		if len(self.NounList) > 0 and len(self.AdjList) > 0:
			iNumAdjs = randint(1, 3)
			iNounIndex = randint(0, len(self.NounList) - 1)
			
			x = randint(1, 6)
			if x == 6 and iNumAdjs != 3:
				sFloweryDesc += self.DefaultAdj + " "
			
			for i in range(0, iNumAdjs):
				iAdjIndex = randint(0, len(self.AdjList) - 1)
				
				while self.AdjList[iAdjIndex] in sFloweryDesc:
					iAdjIndex = randint(0, len(self.AdjList) - 1)
				
				sFloweryDesc += self.AdjList[iAdjIndex]
								
				if i <= iNumAdjs - 1:
					sFloweryDesc += " "
			
			sFloweryDesc += self.NounList[iNounIndex]
		else:
			print("WARNING: NounList OR AdjList lengths are 0")
			sFloweryDesc = ""
			
		return sFloweryDesc
	
	def RandomDescription(self, bAllowShortDesc = True, bAllowLongDesc = True):
		sRandomDesc = ""
		
		if bAllowShortDesc:
			sRandomDesc = self.DefaultNoun
		else:
			sRandomDesc = self.MediumDescription()
		
		iRand = randint(0, 9)
		
		if iRand in range(0, 3):
			if bAllowShortDesc:
				sRandomDesc = self.ShortDescription()
			else:
				sRandomDesc = self.MediumDescription()
		elif iRand in range(3, 8):
			sRandomDesc = self.MediumDescription()
		elif iRand in range(8, 9):
			if bAllowLongDesc:
				sRandomDesc = self.FloweryDescription()
			else:
				sRandomDesc = self.MediumDescription()
			
		return sRandomDesc

class Skin(BodyParts):
	def __init__(self):
		self.NounList = ['skin',
			'flesh']
			
		self.AdjList = ['almond-colored',
			'bare',
			'bronzed',
			'chocolate',
			'coffee-colored',
			'dark',
			'delicate',
			'exposed',
			'freckled',
			'gentle',
			'gleaming',
			'glistening',
			'glowing',
			'gossamer',
			'honeyed',
			'luscious',
			'naked',
			'pale',
			'perfect',
			'porcelain',
			'silken',
			'soft',
			'smooth',
			'sun-browned',
			'sun-kissed',
			'supple',
			'sweet',
			'tender',
			'un-blemished',
			'un-sullied',
			'warm',
			'yielding',
			'youthful']
		
		self.DefaultNoun = "skin"
		self.IsPlural = False
		
class Mouth(BodyParts):
	def __init__(self):
		self.NounList = ['mouth',
						 'mouth',
						 'mouth',
						 'mouth',
						 'mouth-hole']
			
		self.AdjList = ['eager',
			'greedy',
			'hungry',
			'insatiable',
			'insolent',
			'lewd',
			'open',
			'wanting',
			'willing']
		
		self.DefaultNoun = "mouth"
		self.DefaultAdj = "insatiable"
		self.IsPlural = False
		
class Lips(BodyParts):
	def __init__(self):
		self.NounList = ['lips',
						 'mouth']
			
		self.AdjList = ['candy-colored',
			'full',
			'inviting',
			'insolent',
			'luscious',
			'red',
			'sensual',
			'sweet']
		
		self.DefaultNoun = "lips"
		self.DefaultAdj = "red"
		
class Eyes(BodyParts):
	def __init__(self):
		self.NounList = ['eyes']
			
		self.AdjList = ['alluring',
			'beautiful',
			'bewitching',
			'blue',
			'brown',
			'captivating',
			'dark',
			'dazzling',
			'enchanting',
			'green',
			'gray',
			'mischievous',
			'soulful',
			'sweet']
		
		self.DefaultNoun = "eyes"
		self.DefaultAdj = "bewitching"
		
class Hips(BodyParts):
	def __init__(self):
		self.NounList = ['hips']
			
		self.AdjList = ['curvy',
			'curvaceous',
			'bare',
			'fertile',
			'rounded',
			'sensual',
			'shapely',
			'slinky',
			'sultry',
			'tantalizing',
			'voluptuous',
			'wanton',
			'wide',
			'womanly']
		
		self.DefaultNoun = "hips"
		
class Hair(BodyParts):
	def __init__(self):
		self.NounList = ['hair',
			'hair',
			'hair',
			'locks']
			
		self.AdjList = ['black',
			'blonde',
			'brunette',
			'curly',
			'dark',
			'elegant',
			'flaming-red',
			'flowing',
			'glossy',
			'golden',
			'kinky',
			'long',
			'luxuriant',
			'red',
			'silken',
			'short',
			'straight',
			'tightly-bound',
			'unbound',
			'vibrant',
			'voluminous',
			'wavy']
		
		self.DefaultNoun = "hair"
		self.DefaultAdj = "flowing"
		
class Legs(BodyParts):
	def __init__(self):
		self.NounList = ['legs',
			'legs',
			'legs',
			'limbs']
			
		self.AdjList = ['agile',
			'athletic',
			'coltish',
			'elegant',
			'flexible',
			'graceful',
			'lithe',
			'limber',
			'lissome',
			'lithesome',
			'long',
			'muscular',
			'pliant',
			'shapely',
			'smooth',
			'silken']
		
		self.DefaultNoun = "legs"
		
class Thighs(BodyParts):
	def __init__(self):
		self.NounList = ['thighs']
			
		self.AdjList = ['athletic',
			'bare',
			'bronzed',
			'chubby',
			'chunky',
			'comely',
			'delectable',
			'full',
			'girlish',
			'heavy',
			'inviting',
			'lissome',
			'lithe',
			'luscious',
			'nubile',
			'pale',
			'powerful',
			'porcelain',
			'ripe',
			'rounded',
			'sensual',
			'shapely',
			'silken',
			'smooth',
			'soft',
			'sultry',
			'tanned',
			'tender',
			'thick',
			'un-sullied',
			'voluptuous',
			'wide',
			'womanly',
			'young',
			'youthful']
		
		self.DefaultNoun = "thighs"
		
class Nipples(BodyParts):
	def __init__(self):
		self.NounList = ['nipples']
			
		self.AdjList = ['blossoming',
			'budding',
			'chocolate',
			'dainty',
			'dark',
			'enormous',
			'erect',
			'exposed',
			'inch-long',
			'long',
			'luscious',
			'pert',
			'pokey',
			'puffy',
			'rosebud'
			'rose-colored'
			'ripe',
			'sensitive',
			'shameless',
			'stiff',
			'succulent',
			'swollen',
			'tasty',
			'tender',
			'tiny',
			'wide']
		
		self.DefaultNoun = "nipples"
		self.DefaultAdj = "erect"
		
class Breasts(BodyParts):
	Nipples = []
	
	def __init__(self):
		self.NounList = ['bosoms',
			'bosoms',
			'breasts',
			'breasts',
			'breasts',
			'breasts',
			'buds',
			'bust',
			'chest',
			'coconuts',
			'mammaries',
			'melons',
			'orbs',
			'rack',
			'teats',
			'tits',
			'tits']
			
		self.AdjList = ['bare',
			'bouncy',
			'bountiful',
			'budding',
			'buxom',
			'delicious',
			'double-D',
			'exposed',
			'fake',
			'fucking',
			'full',
			'fulsome',
			'generous',
			'gentle',
			'girlish',
			'gorgeous',
			'heaving',
			'heavy',
			'impressive',
			'jiggling',
			'juicy',
			'luscious',
			'lush',
			'luxuriant',
			'magnificent',
			'naked',
			'nubile',
			'pale',
			'pendulous',
			'perky',
			'pert',
			'plump',
			'proud',
			'quivering',
			'ripe',
			'round',
			'sensual',
			'shapely',
			'smooth',
			'soft',
			'stacked',
			'statuesque',
			'stunning',
			'succulent',
			'sumptuous',
			'supple',
			'swaying',
			'sweet',
			'swollen',
			'tender',
			'voluptuous',
			'womanly']
		
		self.DefaultNoun = "breasts"
		self.Nipples = Nipples() 
		
class Clitoris(BodyParts):
	def __init__(self):
		self.NounList = ['clit',
			'clit',
			'clitoris',
			'clitoris',
			'love-button',
			'love-nub',
			'magic button',
			'nub',
			'pearl']
			
		self.AdjList = ['delicate',
			'engorged',
			'engorged',
			'erect',
			'exposed',
			'fevered',
			'pink',
			'pulsating',
			'pulsing',
			'secret',
			'sensitive',
			'shy little',
			'swollen',
			'tender',
			'throbbing',
			'tingling']
		
		self.DefaultNoun = "clit"
		self.IsPlural = False

class VaginaInner(BodyParts):

	def __init__(self):
			self.NounList = ['cherry',
				'cock-sock',
				'cunt-hole',
				'fuck-tunnel',
				'fuckhole',
				'furrow',
				'gash',
				'hole',
				'honey hole',
				'honeypot',
				'love-channel',
				'love-tunnel',
				'slit',
				'trench',
				'tunnel',
				'vagina',
				'vaginal canal',
				'vestibule',
				'womb']
			self.AdjList = ['cherry',
				'cherry red',
				'clenched',
				'deep',
				'delicate',
				'dewy',
				'dripping',
				'fuckable',
				'glazed',
				'gushing',
				'honeyed',
				'hungry',
				'juicy',
				'leaky',
				'lewd',
				'lush',
				'lustful',
				'moist',
				'oozing',
				'pink',
				'secret',
				'silk',
				'snug',
				'sopping',
				'spread',
				'succulent',
				'sweet',
				'tender',
				'tight',
				'velvet',
				'virginal',
				'wanton',
				'well-used']
			
			self.DefaultNoun = "vaginal canal"
			self.IsPlural = False
	
class VaginaOuterLabia(BodyParts):

	def __init__(self):
			self.NounList = ['labia',
							 'lips',
							 'mons pubis',
							 'mound',
							 'nether lips',
							 'outer labia',
							 'outer pussy lips',
							 'pussy lips',
							 'vulva']
			self.AdjList = ['bare',
							'dewy',
							'downy',
							'down-thatched',
							'dripping',
							'fur-lined',
							'girlish',
							'gleaming wet',
							'glistening',
							'hairless',
							'honeyed',
							'juicy',
							'lickable',
							'luscious',
							'lush',
							'moist',
							'naked',
							'peach-fuzzed',
							'pink',
							'puffy',
							'shameless',
							'shaved',
							'shaven',
							'silken',
							'slick',
							'smooth',
							'succulent',
							'suckable',
							'supple',
							'sweet',
							'swollen',
							'tender',
							'trim',
							'wet']
			
			self.DefaultNoun = "mons pubis"

class VaginaInnerLabia(BodyParts):

	def __init__(self):
			self.NounList = ['beef-curtains',
							 'butterfly wings',
							 'cunt-lips',
							 'cunt-flaps',
							 'flaps',
							 'flower petals',
							 'folds',
							 'fringe',
							 'inner labia',
							 'labia',
							 'lips',
							 'meat curtains',
							 'meat-flaps',
							 'nether-lips',
							 'petals',
							 'piss-flaps',
							 'pussy lips',
							 'sex-lips',
							 'wizard sleeve']
			self.AdjList = ['beefy',
							'chewy',
							'dangling',
							'dark',
							'delicate',
							'dewy',
							'dewy',
							'dripping',
							'drooping',
							'droopy',
							'gleaming wet',
							'glistening',
							'gossamer',
							'honeyed',
							'juicy',
							'lickable',
							'little',
							'long',
							'lush',
							'meaty',
							'moist',
							'pink',
							'purple',
							'ruffled',
							'secret',
							'shameless',
							'silken',
							'shy',
							'succulent',
							'suckable',
							'tender',
							'trim',
							'velvet']
			self.DefaultNoun = "inner labia"
			
class Vagina(BodyParts):
	InnerVag = []
	InnerLabia = []
	OuterLabia = []
	Clitoris = []
	
	def __init__(self):
		self.NounList = ['cherry pie',
					'cooch',
					'coochie',
					'cunny',
					'cunt',
					'entrance',
					'flower',
					'fuckhole',
					'hole',
					'honeypot',
					'love-muffin'
					'muff',
					'muffin',
					'peach',
					'pie',
					'pussy',
					'quim',
					'sex',
					'snatch',
					'trench',
					'twat',
					'vagina',
					'womanhood']
					   
		self.AdjList =  ['bare',
					'cherry',
					'clenched',
					'delightful',
					'dewy',
					'down-thatched',
					'dripping',
					'exposed',
					'fuckable',
					'fur-lined',
					'girlish',
					'glazed',
					'gleaming wet',
					'glistening',
					'gushing',
					'hairless',
					'honeyed',
					'horny',
					'hungry',
					'juicy',
					'leaky',
					'lewd',
					'lickable',
					'luscious',
					'lush',
					'lustful',
					'moist',
					'naked',
					'peach-fuzzed',
					'pink',
					'pink',
					'puffy',
					'secret',
					'shameless',
					'silken',
					'slick',
					'smooth',
					'sopping',
					'succulent',
					'suckable',
					'supple',
					'sweet',
					'swollen',
					'tender',
					'tight',
					'trim',
					'unsullied',
					'velvet',
					'virginal',
					'wanton',
					'well-used',
					'willing']
		
		self.DefaultNoun = "vagina"
		self.IsPlural = False
		self.InnerVag = VaginaInner()
		self.OuterLabia = VaginaOuterLabia()
		self.InnerLabia = VaginaInnerLabia()
		self.Clitoris = Clitoris()


class AnusFemale(BodyParts):
	def __init__(self):
		self.NounList = ['anus',
			'anus',
			'anus',
			'arse-cunt',
			'asshole',
			'back orifice',
			'back passage',
			'backdoor',
			'bowels',
			'bunghole',
			'butthole',
			'butt hole',
			'corn hole',
			'crack',
			'crevice',
			'dirt-pipe',
			'fart blaster',
			'fissure',
			'heinie hole',
			'hole',
			'knot',
			'poop-chute',
			'rear orifice',
			'rear passage',
			'rectum',
			'ring',
			'rosebud',
			'sphincter',
			'sphincter',
			'starfish',
			'starfish']
			
		self.AdjList = ['clenched',
			'forbidden',
			'fuckable',
			'gaping',
			'knotted',
			'lewd',
			'little',
			'loose',
			'nasty',
			'naughty',
			'pert',
			'puckered',
			'shy',
			'smooth',
			'snug',
			'taboo',
			'tender',
			'tight',
			'virginal',
			'wanton',
			'well-used',
			'willing',
			'winking']
		
		self.DefaultNoun = "anus"
		self.IsPlural = False
		
class AssFemale(BodyParts):
	Anus = []
	
	def __init__(self):
		self.NounList = ['ass',
			'backside',
			'behind',
			'booty',
			'bottom',
			'bum',
			'buns',
			'butt',
			'buttocks',
			'cheeks',
			'heinie',
			'rump',
			'tush',
			'tushy']
			
		self.AdjList = ['bare',
			'bountiful',
			'broad',
			'bubble-shaped',
			'curvaceous',
			'curvy',
			'exposed',
			'fuckable',
			'generous',
			'glistening',
			'honeyed',
			'lush',
			'naked',
			'nubile',
			'pert',
			'plump',
			'ripe',
			'rosy',
			'rotund',
			'round',
			'shameless',
			'shapely',
			'smooth',
			'succulent',
			'supple',
			'sweet',
			'tender',
			'thick',
			'trim',
			'virginal',
			'womanly']
		
		self.DefaultNoun = "ass"
		self.Anus = AnusFemale() 
		
class BodyFemale(BodyParts):
	Hair = []
	Face = []
	Eyes = []
	Lips = []
	Mouth = []
	Skin = []
	Hips = []
	Legs = []
	Thighs = []
	Breasts = []
	Vagina = []
	Ass = []
	
	def __init__(self):
		self.NounList = ['anatomy',
			'body',
			'body',
			'body',
			'body',
			'curves',
			'figure',
			'flesh',
			'form',
			'physique']
			
		self.AdjList = ['bare',
			'beautiful',
			'busty',
			'buxom',
			'curvaceous',
			'curvy',
			'exposed',
			'feminine',
			'girlish',
			'glistening',
			'gorgeous',
			'honeyed',
			'leggy',
			'lush',
			'luxuriant',
			'model-esque',
			'naked',
			'nubile',
			'pale',
			'ravishing',
			'ripe',
			'sensual',
			'sexy',
			'shameless',
			'shapely',
			'slender',
			'statuesque',
			'stunning',
			'succulent',
			'sultry',
			'supple',
			'sweet',
			'tender',
			'tight',
			'trim',
			'voluptuous',
			'willing',
			'womanly']
		
		self.DefaultNoun = "body"
		self.IsPlural = False
		self.Hair = Hair()
		self.Eyes = Eyes()
		self.Lips = Lips()
		self.Mouth = Mouth()
		self.Hips = Hips()
		self.Legs = Legs()
		self.Skin = Skin()
		self.Thighs = Thighs()
		self.Breasts = Breasts()
		self.Vagina = Vagina()
		self.Ass = AssFemale()
		
	def GetRandomBodyParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc))
		else:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
		
	def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc))
		else:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
	def GetHoles(self, bIncludeMouth = True):
		Holes = []
		
		if bIncludeMouth:
			Holes = [3]
		
			Holes[0] = self.Mouth.RandomDescription()
			Holes[1] = self.Vagina.RandomDescription()
			Holes[2] = self.Ass.Anus.RandomDescription()
		else:
			Holes = [2]
			
			Holes[0] = self.Vagina.RandomDescription()
			Holes[1] = self.Ass.Anus.RandomDescription()
		
		return Holes
		
	def GetRandomHole(self, bIncludeMouth = True, bAllowShortDesc = True):
		sHole = ""
		Holes = []
		if bIncludeMouth:		
			Holes.append(self.Mouth.RandomDescription(bAllowShortDesc))
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc))
		else:
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc))
		
		iRand = randint(0, len(Holes) - 1)
		sHole = Holes[iRand]
		
		return sHole
		
class PenisHead(BodyParts):
	def __init__(self):
		self.NounList = ['cock-head',
			'head',
			'head',
			'head',
			'helmet',
			'knob',
			'knob',
			'mushroom',
			'tip',
			'tip']
			
		self.AdjList = ['bulging',
			'dripping',
			'engorged',
			'glistening',
			'pulsating',
			'purple',
			'smooth',
			'swollen',
			'throbbing',
			'tumescent']
		
		self.DefaultNoun = "head"
		self.IsPlural = False
		
class Testicles(BodyParts):
	def __init__(self):
		self.NounList = ['balls',
			'ballsack',
			'bollocks',
			'gonads',
			'nutsack',
			'sack',
			'silk purse',
			'scrotum',
			'testicles']
			
		self.AdjList = ['dangling',
			'downy',
			'down-covered',
			'fleshy',
			'hairy',
			'heavy',
			'hefty',
			'pendulous',
			'round',
			'satin',
			'silken',
			'soft',
			'smooth',
			'swaying',
			'swinging',
			'tender',
			'wrinkled']
		
		self.DefaultNoun = "testicles"

class Penis(BodyParts):
	Head = []
	Testicles = []
	PenisFrontPart = []
	PenisBackPart = []
	
	def BuildAPenis(self):
		iRandFront = 0
		iRandBack = 0
		
		for i in range(0, int(len(self.NounList) * (2/3))):
			iRandFront = randint(0,len(self.PenisFrontPart) - 1)
			iRandBack = randint(0,len(self.PenisBackPart) - 1)
			sFrontPart = self.PenisFrontPart[iRandFront]
			sBackPart = self.PenisBackPart[iRandBack]
			
			while sFrontPart in sBackPart:
				iRandFront = randint(0,len(self.PenisFrontPart) - 1)
				iRandBack = randint(0,len(self.PenisBackPart) - 1)
				sFrontPart = self.PenisFrontPart[iRandFront]
				sBackPart = self.PenisBackPart[iRandBack]
				
			sPenis = sFrontPart + "-" + sBackPart
			
			while sPenis in self.NounList:
				iRandFront = randint(0,len(self.PenisFrontPart) - 1)
				iRandBack = randint(0,len(self.PenisBackPart) - 1)
				sFrontPart = self.PenisFrontPart[iRandFront]
				sBackPart = self.PenisBackPart[iRandBack]
				
				while sFrontPart in sBackPart:
					iRandFront = randint(0,len(self.PenisFrontPart) - 1)
					iRandBack = randint(0,len(self.PenisBackPart) - 1)
					sFrontPart = self.PenisFrontPart[iRandFront]
					sBackPart = self.PenisBackPart[iRandBack]
					
				sPenis = sFrontPart + "-" + sBackPart
			
			self.NounList.append(sPenis)
		
	def __init__(self):
		self.NounList = ['boner',
			'cock',
			'cock',
			'cock',
			'cock meat',
			'cocksicle',
			'dick',
			'erection',
			'girth',
			'goo-gun',
			'hardness',
			'hard-on',
			'hot-rod',
			'joystick',
			'lady-dagger',
			'love-gun',
			'meat',
			'member',
			'organ',
			'package',
			'penis',
			'penis',
			'penis',
			'phallus',
			'pole',
			'popsicle',
			'prick',
			'ramrod',
			'rod',
			'schlong',
			'serpent',
			'shaft',
			'snake',
			'stalk',
			'stem',
			'thing',
			'tool',
			'wood']
			
		self.AdjList = ['beautiful',
			'beefy',
			'bulging',
			'burning',
			'carefully man-scaped',
			'engorged',
			'enormous',
			'enormously erect',
			'erect',
			'erect',
			'fat',
			'fevered',
			'fucking',
			'fully erect',
			'hairy',
			'hairless',
			'hard',
			'hardening',
			'hardened',
			'huge',
			'hugely erect',
			'impressive',
			'lengthy',
			'long',
			'lovingly man-scaped',
			'magnificient',
			'massive',
			'massively erect',
			'meaty',
			'pulsating',
			'raging',
			'rampant',
			'rigid',
			'rock-hard',
			'silken',
			'smooth',
			'stiff',
			'swollen',
			'tall',
			'tasty',
			'thick',
			'throbbing',
			'towering',
			'tumescent',
			'turgid',
			'unfurled',
			'veiny',
			'virile']
			
		self.PenisFrontPart = ['beef',
			'flesh',
			'fuck',
			'love',
			'man',
			'meat']
			
		self.PenisBackPart = ['bayonette',
			'bone',
			'hammer',
			'lance',
			'meat',
			'missile',
			'pipe',
			'pistol',
			'pole',
			'popsicle',
			'python',
			'rocket',
			'rod',
			'rifle',
			'sausage',
			'serpent',
			'shaft',
			'snake',
			'stack',
			'stalk',
			'stick',
			'sword',
			'tool',
			'tube',
			'weapon',
			'worm']
		
		self.DefaultNoun = "cock"
		self.IsPlural = False
		self.Head = PenisHead()
		self.Testicles = Testicles()
		
		self.BuildAPenis()
	
	def GetRandomPenisPart(self, bAllowShortDesc = False):
		iRand = randint(1,3)
		
		if iRand == 1:
			return self.Head.RandomDescription(bAllowShortDesc)
		elif iRand == 2: 
			return self.Testicles.RandomDescription(bAllowShortDesc)
		else:
			return self.RandomDescription(bAllowShortDesc)
	
class Semen(BodyParts):
	def __init__(self):
		self.NounList = ['cock milk',
			'cock-snot',
			'cream',
			'cum',
			'jizm',
			'jizz',
			'load',
			'lotion',
			'man-custard',
			'man-jam',
			'man-milk',
			'man-seed',
			'seed',
			'semen',
			'sperm',
			'splooge',
			'spunk']
			
		self.AdjList = ['glossy',
			'gooey',
			'milky',
			'nasty',
			'pearlescent',
			'pearly',
			'salty',
			'silken',
			'silky',
			'sticky',
			'warm',
			'white hot']
		
		self.DefaultNoun = "semen"
		self.DefaultAdj = "gooey"
		
class AssMale(BodyParts):
	def __init__(self):
		self.NounList = ['ass',
			'backside',
			'behind',
			'bottom',
			'bum',
			'buns',
			'butt',
			'butt cheeks',
			'buttocks',
			'glutes',
			'gluteous maximus',
			'rump',
			'tush']
			
		self.AdjList = ['beefy',
			'broad',
			'bronzed',
			'chiseled',
			'compact',
			'hairy',
			'lean',
			'manly',
			'masculine',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'rock-hard',
			'smooth',
			'strapping',
			'supple',
			'taut',
			'tight',
			'trim',
			'virile',
			'well-defined']
		
		self.DefaultNoun = "buttocks"
		
class SkinMale(BodyParts):
	def __init__(self):
		self.NounList = ['skin',
			'skin',
			'skin',
			'flesh',
			'hide']
			
		self.AdjList = ['bare',
			'bronzed',
			'coffee-colored',
			'dark',
			'ebony',
			'exposed',
			'freckled',
			'glistening',
			'hairy',
			'naked',
			'rough',
			'rugged',
			'smooth',
			'sun-browned',
			'supple',
			'tough',
			'warm',
			'youthful']
		
		self.DefaultNoun = "skin"
		self.DefaultAdj = "rugged"
		
class ShouldersMale(BodyParts):
	def __init__(self):
		self.NounList = ['shoulders']
			
		self.AdjList = ['bare',
			'brawny',
			'broad',
			'bronzed',
			'freckled',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rugged',
			'strong',
			'sturdy',
			'sun-browned',
			'well-built',
			'wide']
		
		self.DefaultNoun = "shoulders"
		self.DefaultAdj = "broad"
		
class ChestMale(BodyParts):
	def __init__(self):
		self.NounList = ['chest',
			'chest',
			'chest',
			'chest',
			'pectorals']
			
		self.AdjList = ['bare',
			'brawny',
			'broad',
			'bronzed',
			'burly',
			'compact',
			'dark-thatched',
			'expansive',
			'hairy',
			'lusty',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'ripped',
			'rugged',
			'strapping',
			'strong',
			'sturdy',
			'toned',
			'wide',
			'uncovered',
			'virile',
			'well-built',
			'well-defined',
			'well-oiled']
		
		self.DefaultNoun = "chest"
		self.DefaultAdj = "broad"
		
class ArmsMale(BodyParts):
	def __init__(self):
		self.NounList = ['arms',
			'arms',
			'arms',
			'arms',
			'limbs']
			
		self.AdjList = ['athletic',
			'bare',
			'brawny'
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'protective',
			'rippling',
			'ripped',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry']
		
		self.DefaultNoun = "arms"
		self.DefaultAdj = "muscular"
		
class EyesMale(BodyParts):
	def __init__(self):
		self.NounList = ['eyes']
			
		self.AdjList = ['beautiful',
			'blue',
			'brooding',
			'brown',
			'captivating',
			'dark',
			'dazzling',
			'green',
			'gray',
			'icy blue',
			'kind',
			'mischievous',
			'penetrating',
			'soulful',
			'steely-blue',
			'stern',
			'youthful']
		
		self.DefaultNoun = "eyes"
		self.DefaultAdj = "penetrating"
		
class LegsMale(BodyParts):
	def __init__(self):
		self.NounList = ['legs',
			'legs',
			'legs',
			'calves',
			'limbs',
			'thighs']
			
		self.AdjList = ['athletic',
			'bare',
			'brawny',
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rangy',
			'rippling',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry']
		
		self.DefaultNoun = "legs"
		self.DefaultAdj = "sinewy"
		
class JawMale(BodyParts):
	def __init__(self):
		self.NounList = ['jaw']
			
		self.AdjList = ['bearded',
			'chiseled',
			'commanding',
			'decisive',
			'dominant',
			'forceful',
			'handsome',
			'powerful',
			'rugged',
			'scruffy',
			'sharp',
			'striking']
		
		self.DefaultNoun = "jaw"
		self.DefaultAdj = "chiseled"
		
class BodyMale(BodyParts):
	Hair = []
	Face = []
	Eyes = []
	Jaw = []
	Skin = []
	Shoulders = []
	Arms = []
	Chest = []
	Legs = []
	Ass = []
	Penis = []
	
	def __init__(self):
		self.NounList = ['body',
			'form',
			'physique',
			'anatomy',
			'bulk',
			'build',
			'body',
			'physique',
			'build',
			'form',
			'body']
			
		self.AdjList = ['beefy',
			'brawny',
			'broad',
			'bronzed',
			'burly',
			'commanding',
			'compact',
			'dark-thatched',
			'handsome',
			'hung',
			'lean',
			'limber',
			'manly',
			'masculine',
			'massive',
			'muscular',
			'powerful',
			'rugged',
			'sinewy',
			'smooth',
			'strapping',
			'striking',
			'strong',
			'sturdy',
			'supple',
			'tall',
			'taut',
			'tight',
			'toned',
			'towering',
			'trim',
			'virile',
			'well-built',
			'well-hung',
			'well-oiled',
			'wiry',
			'youthful']
		
		self.DefaultNoun = "body"
		self.IsPlural = False
		#self.Hair = Hair()
		self.Eyes = EyesMale()
		self.Jaw = JawMale()
		self.Legs = LegsMale()
		self.Skin = SkinMale()
		self.Shoulders = ShouldersMale()
		self.Chest = ChestMale()
		self.Arms = ArmsMale()
		self.Ass = AssMale()
		self.Penis = Penis()
		
	def GetRandomBodyParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc))
		else:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
	def GetRandomIntimateParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc))
		else:
			AllParts.append(self.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts