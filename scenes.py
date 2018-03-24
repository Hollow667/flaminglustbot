# Locations module

import bodyparts
import locations
import names
import people
import verbs
import misc

from random import * 
from util import *

class Scene():
	Location = None
	HisName = "he"
	HerName = "she"
	HisNamePos = "his"
	HerNamePos = "her"
	SceneShortDescPresent = ""
	SceneShortDescPast = ""
	SceneShortDescGerund = ""
	
	def __init__(self, sHisName = "", sHerName = "", oLocation = None):
		if not sHisName == "":
			self.HisName = sHisName
			self.HisNamePos = self.HisName + "'s"
		if not sHerName == "":
			self.HerName = sHerName
			self.HerNamePos = self.HerName + "'s"
			
		if oLocation == None:
			pass
		else:
			self.Location = oLocation
			
	def Scene(self):
		sScene = ""
		
		return sScene
		
	def ShortScene(Vtense = Tense.Past):
		pass
		
class SceneCreamPie(Scene):
	SemenGobs = WordList(['beads', 'drops', 'globules', 'gobs', 'pearls', 'ropes', 'strings', 'trails'])
	DripVerbs = WordList(['dribbled', 'dripped', 'flowed', 'gushed', 'hung', 'leaked', 'oozed', 'poured'])
	
	def ShortScene(Vtense = Tense.Past):
		sScene = ""
		Hole = None
		
		if bIsPussy:
			Hole = bodyparts.BodyFemale().Vagina
		else:
			Hole = bodyparts.BodyFemale().Ass.Anus
		
		if Vtense == Tense.Gerund:
			sScene = self.HisName + " was cream pie-ing " + self.HerNamePos + " " + Hole.MediumDescription()
		elif Vtense == Tense.Past:
			sScene = self.HisName + " cream-pied " + self.HerNamePos + " " + Hole.MediumDescription()
		else:
			sScene = self.HisName + " cream-pies " + self.HerNamePos + " " + Hole.MediumDescription()
			
		if not self.Location is None:
			sScene += " on the " + Location.Ground
			
		return sScene
	
	def Scene(self, bIsVagina = True):
		Penis = bodyparts.Penis()
		Semen = bodyparts.Semen()
		Vagina = bodyparts.Vagina()
		Anus = bodyparts.AnusFemale()
		Thighs = bodyparts.Thighs()
		sScene = ""
		
		sScene = Semen.GetAdj().capitalize() + " " + self.SemenGobs.GetWord() +" of " + Semen.GetNoun() + " " + self.DripVerbs.GetWord() + " from " + self.HerNamePos 
		
		if bIsVagina:
			iRandPussyDesc = randint(1, 3)
			
			if iRandPussyDesc == 1:
				sScene += " " + Vagina.RandomDescription(bAllowShortDesc = True)
			elif iRandPussyDesc == 2:
				sScene += " " + Vagina.InnerLabia.RandomDescription(bAllowShortDesc = True)
			else:
				sScene += " " + Vagina.InnerVag.RandomDescription(bAllowShortDesc = True)
		else:
			sScene += " " + Anus.RandomDescription(bAllowShortDesc = True)
		
		iRandAfter = randint (1,10)
		
		if iRandAfter % 2 == 0:
			sScene += " and down her " + Thighs.RandomDescription(bAllowShortDesc = True)
		if iRandAfter > 4:
			if not self.Location == None:
				sScene += " and onto the " + self.Location.Ground 
		if iRandAfter % 3 == 0: 
			sScene += ". She scooped some up with her fingers and tasted it"
		if iRandAfter > 6:
			sScene += ". " + self.HerName + " got down on her knees and began to lick the " + Semen.RandomDescription() + " from his " + Penis.RandomDescription()
		
		#print("sScene[len(sScene) - 1] = " + sScene[len(sScene) - 1])
		if not sScene[len(sScene) - 1] == ".":
			sScene += "."
			
		return sScene
	
class SceneAnal(Scene):

	def ShortScene(self, Vtense = Tense.Past):
		sScene = ""
		
		Penis = bodyparts.Penis()
		Anus = bodyparts.AnusFemale()
		VerbThrust = verbs.VerbThrust()
		
		if Vtense == Tense.Gerund:
			sScene = self.HisName + " was " + VerbThrust.Gerund() + " " + self.HerNamePos + " " + Anus.RandomDescription(bAllowShortDesc) + " with his " + Penis.RandomDescription(bAllowShortDesc = True)
		elif Vtense == Tense.Present:
			sScene = self.HisName + " proceeded to " + VerbThrust.Present() + " " + self.HerNamePos + " " + Anus.RandomDescription(bAllowShortDesc) + " with his " + Penis.RandomDescription(bAllowShortDesc = True)
		else:
			sScene = self.HisName + " " + VerbThrust.Past() + " " + self.HerNamePos + " " + Anus.RandomDescription(bAllowShortDesc = True) + " with his " + Penis.RandomDescription(bAllowShortDesc = True)
			
		return sScene
		
	def Scene(self):
		sScene = ""
		
		Penis = bodyparts.Penis()
		Ass = bodyparts.AssFemale()
		Anus = bodyparts.AnusFemale()
		Clit = bodyparts.Clitoris()
		VerbThrust = verbs.VerbThrust()
		
		AdvSpread = WordList(["lovingly", "carefully", "tenderly", "forcefully", "firmly", "gently", "expertly", "roughly"])
		
		Actions = []
		
		if CoinFlip():
			Actions.append(self.HisName + " " + AdvSpread.GetWord() + " spread " + self.HerNamePos + " " + Ass.RandomDescription() + " apart, ")
		else: 
			Actions.append(self.HerName + " winked at him as she " + AdvSpread.GetWord() + " spread her " + Ass.RandomDescription() + " apart, ")
		
		Actions.append("exposing her " + Anus.RandomDescription() + ". ")
		
		if CoinFlip():
			if CoinFlip():
				Actions.append(self.HisName + " spit on his fingers")
			else:
				Actions.append(self.HisName + " applied some lube to his fingers")
				
			Actions.append(", and then gently inserted " + str(randint(1,4)) + " of them into " + self.HerNamePos + " " + Anus.ShortDescription() + ". ")
			
		if CoinFlip():
			Actions.append("When she was ready, he eased the " + Penis.Head.RandomDescription() + " of his " + Penis.ShortDescription() + " into her tight " + Anus.ShortDescription() + ". ")
			
		Actions.append("Before long ")
		
		if CoinFlip():
			Actions.append("he was " + VerbThrust.Gerund() + " her " + Anus.ShortDescription() + " " + AdvSpread.GetWord())
		else:
			Actions.append("he was deep in her " + Ass.RandomDescription() + ", fucking her " + AdvSpread.GetWord())
			
		if CoinFlip():
			Actions.append(", stretching her " + Anus.ShortDescription() + " wide")
			
		if CoinFlip():
			Actions.append(" as he diddled her " + Clit.ShortDescription() + " with his hand")
			
		for x in range(0, len(Actions)):
			sScene += Actions[x]
			
		sScene += "."
			
		return sScene

class SceneBlowjob(Scene):

	def ShortScene(self, Vtense = Tense.Past):
		sScene = ""
		
		Penis = bodyparts.Penis()
		
		if Vtense == Tense.Gerund:
			sScene = self.HerName + " was " + verbs.VerbOralMale().Gerund() + " " + self.HisNamePos + " " + Penis.MediumDescription()
		elif Vtense == Tense.Present:
			sScene = self.HerName + " proceeded to " + verbs.VerbOralMale().Present() + " " + self.HisNamePos + " " + Penis.MediumDescription()
		else:
			sScene = self.HerName + " was " + verbs.VerbOralMale().Past() + " " + self.HisNamePos + " " + Penis.MediumDescription()
			
		return sScene
	
	def Scene(self):
		sScene = ""
		
		Actions = []
		
		Penis = bodyparts.Penis()
		Breasts = bodyparts.Breasts()
		
		sScene = self.HerName.capitalize() + " proceeded to " + verbs.VerbOralMale().Present() + " him. "
		
		if CoinFlip():
			Actions.append("She tenderly kissed his " + Penis.Head.RandomDescription() + ". ")
			
		if CoinFlip():
			Actions.append("She rubbed his " + Penis.MediumDescription() + " between her " + Breasts.RandomDescription() + ". ")
			
		if CoinFlip():
			Actions.append("She gave the underside of his " + Penis.ShortDescription() + " a long, loving stroke with her tongue. ")
			
		if CoinFlip():
			Actions.append("She lovingly cupped his " + Penis.Testicles.RandomDescription(bAllowShortDesc = True)+ ". ")
			
		if CoinFlip():
			Actions.append("She was licking and kissing every inch of " + self.HisNamePos + " " + Penis.RandomDescription(bAllowShortDesc = True) + ". ")
			
		Actions.append("She took his " + Penis.ShortDescription() + " into her mouth and began to suck it enthusiastically")
		
		if CoinFlip():
			Actions.append(", taking it so deep into her throat that " + self.HisNamePos + " " + Penis.Testicles.ShortDescription() + " were slapping against her chin. ")
		else:
			Actions.append(". ")
			
		if CoinFlip():
			Actions.append("She caressed and sucked on his " + Penis.Testicles.ShortDescription() + ". ")
			
		for x in range(0, len(Actions)):
			sScene += Actions[x]
			
		sScene += "Before long, thick strands of her saliva were hanging from the length of his " + Penis.ShortDescription() + "."
		
		return sScene 
		
		
		
		
		
		
		
	
	
	
	
	
#class SceneCumOnHer(Scene):
#class SceneCunnilingus(Scene):	
#class SceneForeplay(Scene):
#class SceneMakeOut(Scene):
#class SceneSitOnFace(Scene):
#class SceneTittyFuck(Scene):

#class SceneSexAct(Scene):

		
class SceneSelector():
	Scenes = []
	
	def __init__(self):
		for sub in Scene.__subclasses__():
			self.Scene.Scenes(sub())
	
	def Location(self):
		iRand = randint(0, len(self.Scenes) - 1)
		
		return self.Scenes[iRand]
	

		