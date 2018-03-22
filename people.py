# People module

from random import *
import util

class Person:
	PersonList = []
	
	def GetPerson(self):
		sPerson = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.PersonList) - 1)
		
		sPerson = self.PersonList[iRandIndex]
		
		return sPerson
		
class FemaleFWB(Person):
	PersonList = ['aunt',
		'babysitter',
		'barista',
		'boss',
		'boss\'s wife',
		'CEO',
		'co-ed student',
		'cousin',
		'cute roommate',
		'dad\'s girlfriend',
		'daughter',
		'daughter\'s best friend',
		'daughter-in-law',
		'dominatrix',
		'eighth-grade teacher',
		'English teacher',
		'ex',
		'fashion model',
		'flight attendant',
		'French maid',
		'girlfriend',
		'girlfriend\'s mom',
		'girlfriend\'s sister',
		'guidance counselor',
		'hot best friend',
		'intern',
		'land lady',
		'librarian',
		'life drawing model',
		'English lit student',
		'maid',
		'marriage counselor',
		'masseuse',
		'math tutor',
		'mom\'s best friend',
		'mother-in-law',
		'next-door neighbor',
		'niece',
		'nurse',
		'parole officer',
		'pastor\'s wife',
		'personal trainer',
		'roommate\'s girlfriend',
		'secretary',
		'sister',
		'sister-in-law',
		'sister\'s hot friend',
		'soccer mom',
		'son\'s principal',
		'step-daughter',
		'step-mom',
		'step-sister',
		'Sunday School teacher',
		'teacher',
		'twin sister',
		'wedding planner',
		'wife',
		'wife\'s Avon Lady',
		'wife\'s pregnancy surrogate']
		
class MaleFWB(Person):
	PersonList = ['attorney',
			'attractive male masseuse',
			'baby daddy',
			'bank teller',
			'barista',
			'best friend\'s fiancé',
			'billionaire fiancé',
			'bodyguard',
			'boss',
			'boy toy',
			'boyfriend',
			'brother',
			'brother-in-law',
			'celebrity crush',
			'co-worker',
			'contractor',
			'daddy',
			'daddy dom',
			'daughter\'s boyfriend',
			'dentist',
			'dom',
			'driver',
			'drug dealer',
			'ex-boyfriend',
			'father',
			'father-in-law',
			'fiancé',
			'friend-with-benefits',
			'geography teacher',
			'girlfriend',
			'guidance counselor',
			'gynecologist',
			'hubby',
			'husband',
			'landlord',
			'life coach',
			'lifeguard',
			'lord',
			'mailman',
			'manager',
			'master',
			'minister',
			'one true love',
			'pastor',
			'pediatrician',
			'personal trainer',
			'photographer',
			'pizza delivery boy',
			'pool boy',
			'priest',
			'prince',
			'proctologist',
			'professor',
			'psychiatrist',
			'shift supervisor',
			'sister\'s boyfriend',
			'son-in-law',
			'step-son',
			'tennis coach',
			'twin brother',
			'uber driver',
			'vice-principal',
			'volleyball coach',
			'yoga teacher']
			
class JobBlueCollar(Person):
	PersonList = ['bag boy',
		'ball boy',
		'bellhop',
		'Starbucks barista',
		'beat cop',
		'blogger',
		'bus driver',
		'cattle wrangler',
		'civil servant',
		'Comcast technician',
		'dog walker',
		'dog groomer',
		'farm hand',
		'farmer',
		'food court worker',
		'fry cook',
		'garbage man',
		'gas station attendant',
		'golf caddy',
		'gym coach',
		'home theater installer',
		'hot dog vendor',
		'high school history teacher',
		'janitor',
		'lawn maintenance man',
		'Lyft driver',
		'manager at Arby\'s',
		'masseur',
		'male nurse',
		'mall santa',
		'mechanic',
		'meter maid',
		'page boy',
		'paige',
		'peasant',
		'pest control technician',
		'pet store clerk',
		'Pizza Hut delivery guy',
		'plumber',
		'pool boy',
		'porn set fluffer',
		'postal clerk',
		'public restroom attendant',
		'rent-a-cop',
		'roadie',
		'roadkill disposal worker',
		'self-published author',
		'serf',
		'server at Applebee\'s',
		'shift supervisor',
		'short-order cook',
		'soldier',
		'stable boy',
		'stand-up comedian',
		'Whole Foods stock boy',
		'tax payer',
		'third-grade teacher',
		'ticket stub collector',
		'tow-truck driver',
		'tour guide',
		'truck driver',
		'used car salesman',
		'waiter',
		'Wal-Mart greeter',
		'writer of erotic romances',
		'zoo keeper']
		
class JobWhiteCollar(Person):
	PersonList = ['accountant',
		'actuary',
		'airline pilot',
		'Apple Store genius',
		'architect',
		'banker',
		'bee keeper',
		'cakery owner',
		'city councilman',
		'civil engineer',
		'classical violinist',
		'crossword puzzle writer',
		'database developer',
		'detective',
		'guru',
		'gynecologist',
		'fashion photographer',
		'flight attendant',
		'house flipper',
		'insurance adjuster',
		'lieutenant colonel',
		'merchant',
		'middle manager',
		'motivational spieaker',
		'opthamologist',
		'orthodonist',
		'pharmacist',
		'photographer',
		'podiatrist',
		'porn star',
		'principal',
		'proctologist',
		'project manager',
		'public radio host',
		'published author',
		'radio DJ',
		'rancher',
		'realtor',
		'regional manager',
		'romance novelist',
		'sex therapist',
		'sex toy designer',
		'sherriff',
		'stage magician',
		'stay-at-home dad',
		'surgeon',
		'tax attorney',
		'tenured professor',
		'urologist',
		'veterinarian',
		'web designer',
		'Wendy\'s franchise owner',
		'yoga teacher']
		
class JobWealthyMale(Person):
	PersonList = ['archduke',
		'baron',
		'Bitcoin billionaire',
		'billionaire',
		'celebrity chef',
		'CEO',
		'count',
		'duke',
		'earl',
		'emperor',
		'executive producer',
		'father superior',
		'film mogul',
		'general',
		'king',
		'knight',
		'marquess',
		'marquis',
		'movie star',
		'Nobel Prize winner',
		'Dalai Lama',
		'pope',
		'porn star',
		'president',
		'prime minister',
		'prince',
		'pro football quarterback',
		'rock star',
		'senator',
		'shah',
		'sheikh',
		'sheriff',
		'sultan',
		'surgeon general',
		'titan of industry',
		'viscount',
		'YouTube star']

class JobWealthyFemale(Person): 
	PersonList = ['actress',
		'archduchess',
		'baroness',
		'heiress',
		'CEO',
		'countess',
		'duchess',
		'empress',
		'fasion designer',
		'first lady',
		'high-born lady',
		'marchioness',
		'mother superior',
		'Nobel Prize winner',
		'porn star',
		'president',
		'princess',
		'prime minister',
		'queen',
		'queen mother',
		'pop star',
		'senator',
		'social media influencer',
		'supermodel',
		'surgeon general',
		'viscountess',
		'wealthy MILF']