# Locations module

import util
import bodyparts
import locations
import names
import people
import verbs
import misc

from random import *

class Scene():
	Location = None
	MaleName = "his"
	FemaleName = "her"
	
	def __init__(self, sHisName = "", sHerName = "", oLocation = None):
		if not sHisName == "":
			MaleName = sHisName
		if not sHerName == "":
			FemaleName = sHerName
			
		if oLocation == None:
			pass
		else:
			self.Location = oLocation
			
	def Scene(self):
		sScene = ""
		
		return sScene
		
class SceneCreamPie(Scene):
	SemenGobs = util.WordList(['beads', 'drops', 'globules', 'gobs', 'pearls', 'ropes', 'strings', 'trails'])
	DripVerbs = util.WordList(['dribbled', 'dripped', 'flowed', 'gushed', 'hung', 'leaked', 'oozed', 'poured'])
	
	def Scene(self, bIsVagina = True):
		Penis = bodyparts.Penis()
		Semen = bodyparts.Semen()
		Vagina = bodyparts.Vagina()
		Anus = bodyparts.AnusFemale()
		Thighs = bodyparts.Thighs()
		sScene = ""
		sFemaleName = ""
		
		if not self.FemaleName == "her":
			sFemaleName = self.FemaleName + "'s"
		else: 
			sFemaleName = self.FemaleName
		
		sScene = Semen.GetAdj().capitalize() + " " + self.SemenGobs.GetWord() +" of " + Semen.GetNoun() + " " + self.DripVerbs.GetWord() + " from " + sFemaleName 
		
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
			sScene += ". She got down on her knees and began to lick the " + Semen.RandomDescription() + " from his " + Penis.RandomDescription()
		
		#print("sScene[len(sScene) - 1] = " + sScene[len(sScene) - 1])
		if not sScene[len(sScene) - 1] == ".":
			sScene += "."
			
		return sScene
	
#class SceneAnal(Scene):
#class SceneBlowjob(Scene):
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
	

		