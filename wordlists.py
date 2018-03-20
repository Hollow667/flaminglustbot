# Word lists module

from random import *

class BodyParts:
	NounList = []
	AdjList = []
	DefaultNoun = ""
	DefaultAdj = "naked"

	def ShortDescription(self):
		#print("Length of NounList is " + str(len(self.NounList)))
		
		sShortDesc = ""
		if len(self.NounList) > 0:
			iNounIndex = randint(0, len(self.NounList) - 1)
			sShortDesc = self.NounList[iNounIndex]
		else: 
			sShortDesc = ""
		return sShortDesc
	
	def MediumDescription(self):
		#print("Length of NounList is " + str(len(self.NounList)))
		#print("Length of AdjList is " + str(len(self.AdjList)))
		sMediumDesc = ""
		
		if len(self.NounList) > 0 and len(self.AdjList) > 0:
			iNounIndex = randint(0, len(self.NounList) - 1)
			iAdjIndex = randint(0, len(self.AdjList) - 1)
			
			sMediumDesc = self.AdjList[iAdjIndex] + ' ' + self.NounList[iNounIndex]
		else:
			sMediumDesc = ""
			
		return sMediumDesc
	
	def FloweryDescription(self):
		#print("Length of NounList is " + str(len(self.NounList)))
		#print("Length of AdjList is " + str(len(self.AdjList)))
		sFloweryDesc = ""
		
		if len(self.NounList) > 0 and len(self.AdjList) > 0:
			#print("NounList and AdjList lengths > 0")
			iNumAdjs = randint(1, 3)
			iNounIndex = randint(0, len(self.NounList) - 1)
			#print("iNumAdjs = " + str(iNumAdjs))
			
			x = randint(1, 6)
			if x == 5 and iNumAdjs != 3:
				#print("Adding 'naked'")
				sFloweryDesc += self.DefaultAdj + " "
			
			#print("iNumAdjs = " + str(iNumAdjs))
			for i in range(0, iNumAdjs):
				#print("i = " + str(i))
				iAdjIndex = randint(0, len(self.AdjList) - 1)
				#print("Randomly selected adj is " + self.AdjList[iAdjIndex])
				
				while self.AdjList[iAdjIndex] in sFloweryDesc:
					#print("Random adj is a duplicate, trying again.")
					iAdjIndex = randint(0, len(self.AdjList) - 1)
				
				sFloweryDesc += self.AdjList[iAdjIndex]
								
				if i <= iNumAdjs - 1:
					sFloweryDesc += " "
				#print("sFloweryDesc is " + sFloweryDesc)
			
			sFloweryDesc += self.NounList[iNounIndex]
		else:
			print("WARNING: NounList OR AdjList lengths are 0")
			sFloweryDesc = ""
			
		return sFloweryDesc
	
	def RandomDescription(self):
		sRandomDesc = "" 
		
		iRand = randint(0, 6)
		
		if iRand in range(0, 2):
			sRandomDesc = self.ShortDescription()
		elif iRand in range(2, 4):
			sRandomDesc = self.MediumDescription()
		elif iRand in range(4, 6):
			sRandomDesc = self.FloweryDescription()
		else:
			sRandomDesc = self.DefaultNoun
			
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
			'supple',
			'sweet',
			'tender',
			'un-blemished',
			'un-sullied',
			'warm',
			'yielding',
			'youthful']
		
		self.DefaultNoun = "skin"
		
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
			'flaming red'
			'flowing',
			'glossy',
			'golden',
			'kinky',
			'long',
			'luxuriant',
			'pixie cut',
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
			
		self.AdjList = ['athletic',
			'coltish',
			'elegant',
			'long',
			'muscular',
			'shapely',
			'smooth',
			'silken']
		
		self.DefaultNoun = "legs"
		self.DefaultAdj = "long"
		
class Thighs(BodyParts):
	def __init__(self):
		self.NounList = ['thighs']
			
		self.AdjList = ['athletic',
			'bare',
			'bronzed',
			'chunky',
			'comely',
			'delectable'
			'full',
			'girlish',
			'heavy',
			'inviting',
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
		
class BodyFemale(BodyParts):
	Hair = []
	Face = []
	Skin = []
	Hips = []
	Legs = []
	Thighs = []
	
	
	def __init__(self):
		self.NounList = ['body',
			'form',
			'shape',
			'physique',
			'curves',
			'anatomy',
			'figure',
			'flesh',
			'body',
			'figure',
			'body',
			'curves']
			
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
		self.Hair = Hair()
		self.Hips = Hips()
		self.Legs = Legs()
		self.Skin = Skin()
		self.Thighs = Thighs()
		
class Nipples(BodyParts):
	def __init__(self):
		self.NounList = ['buds',
			'nipples',
			'nipples',
			'nipples',
			'nipples',
			'nubs']
			
		self.AdjList = ['bare',
			'blossoming',
			'dainty',
			'dark',
			'erect',
			'exposed',
			'long',
			'luscious',
			'pert',
			'puffy',
			'rosebud'
			'rose-colored'
			'ripe',
			'sensitive',
			'stiff',
			'succulent',
			'swollen',
			'tender',
			'wide']
		
		self.DefaultNoun = "nipples"
		
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
			'love button',
			'love nub',
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

class VaginaInner(BodyParts):

	def __init__(self):
			self.NounList = ['vaginal canal',
				'cock-sock',
				'cunt-hole',
				'fuck tunnel',
				'fuckhole',
				'furrow',
				'gash',
				'hole',
				'honey hole',
				'honeypot',
				'inner vagina',
				'love channel',
				'love tunnel',
				'trench',
				'tunnel',
				'womb']
			self.AdjList = ['cherry',
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
				'pink',
				'secret',
				'silk',
				'snug',
				'sopping',
				'spread',
				'succulent',
				'sweet',
				'tender',
				'tender',
				'tight',
				'velvet',
				'virginal',
				'wanton',
				'well-used']
			
			self.DefaultNoun = "vaginal canal"
	
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
			self.AdjList = ['dewy',
							'down-thatched',
							'dripping',
							'exposed',
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
			self.NounList = ['butterfly wings',
							 'cunt lips',
							 'cuntflaps',
							 'flaps',
							 'flower petals',
							 'folds',
							 'fringe',
							 'inner labia',
							 'labia',
							 'lips',
							 'nether lips',
							 'petals',
							 'piss flaps',
							 'pissflaps',
							 'wizard sleeve']
			self.AdjList = ['chewy',
							'dangling',
							'dark',
							'delicate',
							'dewy',
							'drooping',
							'elongated',
							'exposed',
							'gleaming wet',
							'gossamer',
							'honeyed',
							'juicy',
							'lickable',
							'lush',
							'moist',
							'pink',
							'purple',
							'ruffled',
							'secret',
							'shameless',
							'silken',
							'succulent',
							'suckable',
							'supple',
							'sweet',
							'swollen',
							'tender',
							'tender',
							'trim']
			self.DefaultNoun = "inner labia"
			
class Vagina(BodyParts):
	InnerVag = []
	InnerLabia = []
	OuterLabia = []
	Clitoris = []
	
	def __init__(self):
		self.NounList = ['cherry pie',
					'cock-sock',
					'cooch',
					'coochie',
					'cunny',
					'cunt',
					'cunt lips',
					'cunt-hole',
					'entrance',
					'flower',
					'fuckhole',
					'gash',
					'hole',
					'honey hole',
					'honeypot',
					'muff',
					'muffin',
					'nether lips',
					'peach',
					'pie',
					'pussy',
					'pussy lips',
					'quim',
					'sex',
					'slit',
					'snatch',
					'trench',
					'twat',
					'vagina',
					'womanhood',
					'love muffin']
					   
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
		self.InnerVag = VaginaInner()
		self.OuterLabia = VaginaOuterLabia()
		self.InnerLabia = VaginaInnerLabia()
		self.Clitoris = Clitoris()

class AnusFemale(BodyParts):
	def __init__(self):
		self.NounList = ['anus',
			'anus',
			'anus',
			'asshole',
			'back orifice',
			'back passage',
			'backdoor',
			'bunghole',
			'butthole',
			'corn hole',
			'crack',
			'dirt-pipe',
			'fissure',
			'heinie hole',
			'hole',
			'poop chute',
			'rear orifice',
			'ring',
			'rosebud',
			'sphincter',
			'starfish']
			
		self.AdjList = ['forbidden',
			'fuckable',
			'gaping',
			'knotted',
			'lewd',
			'loose',
			'nasty',
			'naughty',
			'pert',
			'shy',
			'smooth',
			'snug',
			'tender',
			'tight',
			'virginal',
			'wanton',
			'well-used',
			'willing',
			'winking']
		
		self.DefaultNoun = "anus"
		
class AssFemale(BodyParts):
	Anus = []
	
	def __init__(self):
		self.NounList = ['arse-cunt',
			'ass',
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
		
		self.DefaultNoun = "anus"
		self.Anus = AnusFemale() 
		
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
		
class Testicles(BodyParts):
	def __init__(self):
		self.NounList = ['balls',
			'ballsack',
			'bollocks',
			'gonads',
			'nutsack',
			'sack',
			'silk purse',
			'testicles']
			
		self.AdjList = ['dangling',
			'fleshy',
			'hairy',
			'heavy',
			'hefty',
			'pendulous',
			'silken',
			'swaying',
			'wrinkled']
		
		self.DefaultNoun = "testicles"

class Penis(BodyParts):
	Head = []
	Testicles = []
	
	def __init__(self):
		self.NounList = ['boner',
			'cock',
			'dick',
			'erection',
			'flesh lance',
			'fuck-pole',
			'fuck-stick',
			'girth',
			'hardness',
			'hard-on',
			'magic wand',
			'man sword',
			'meat',
			'meat pole',
			'meat sword',
			'member',
			'organ',
			'penis',
			'phallus',
			'pole',
			'prick',
			'ramrod',
			'rod',
			'scepter',
			'serpent',
			'shaft',
			'snake',
			'staff',
			'stalk',
			'stem',
			'thing',
			'tool',
			'weapon',
			'wood',
			'love pistol',
			'goo gun']
			
		self.AdjList = ['beefy',
			'bulging',
			'burning',
			'engorged',
			'enormously erect',
			'erect',
			'erect',
			'fat',
			'fevered',
			'fucking',
			'fully erect',
			'hairy',
			'hard',
			'hardened',
			'hugely erect',
			'lengthy',
			'long',
			'magnificient',
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
			'veiny',
			'virile']
		
		self.DefaultNoun = "cock"
		self.Head = PenisHead()
		self.Testicles = Testicles()
		
class Semen(BodyParts):
	def __init__(self):
		self.NounList = ['cock milk',
			'cock snot',
			'cream',
			'cum',
			'jizm',
			'jizz',
			'man custard',
			'man jam',
			'man milk',
			'man seed',
			'seed',
			'semen',
			'sperm',
			'spunk']
			
		self.AdjList = ['glossy',
			'gooey',
			'manly',
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