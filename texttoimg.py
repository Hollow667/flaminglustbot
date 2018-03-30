PATH = "resources/"
FONT = "NoticiaText-Regular.ttf"
TEST_IMAGE = "test.png"
MAX_IMG_NUM = 13

# Text-to-Image module

import os, sys
from PIL import Image, ImageDraw, ImageFont
from random import *

# delete existing test image
def KillTestImg():
	try:
		os.remove(TEST_IMAGE)
	except OSError: 
		pass
		
def WrapText(sText, font, offset_width):
	# break string into multi-lines that fit base_width
	Lines = []
	
	bEndOfText = False
	iLastWhtSpc = 0
	iLineStart = 0
	while not bEndOfText:
		width_of_line = 0
		iLastWhtSpc = iLineStart
		
		for x in range(iLineStart, len(sText)):
			if sText[x].isspace():
				iLastWhtSpc = x
			#print("WrapText() x = " + str(x) + ", iLastWhtSpc = " + str(iLastWhtSpc))
			#print("WrapText() sTest[" + str(x) + "] is '" + sText[x] + "'")
			char_size = font.getsize(sText[x])
			width_of_line += char_size[0]
			
			if sText[x] == "\n" or width_of_line >= offset_width:
				if iLastWhtSpc >= iLineStart:
					#print("WrapText() iLastWhtSpc > iLineStart and line is too wide. Break and append to Lines[]")
					Lines.append(sText[iLineStart:iLastWhtSpc])
					print("WrapText() current line is [" + sText[iLineStart:iLastWhtSpc] + "]")
					iLineStart = iLastWhtSpc + 1
					break
				else:
					#print("WrapText() iLastWhtSpc <= iLineStart and line is too wide. Break and append to Lines[]")
					iLastWhtSpc = int((x - iLineStart)/2) 
					Lines.append(sText[iLineStart:iLastWhtSpc])
					print("WrapText() current line is [" + sText[iLineStart:iLastWhtSpc] + "]")
					iLineStart = iLastWhtSpc + 1
					break
			else:
				#print("WrapText() line is not too wide.")
				if x == len(sText) - 1:
					bEndOfText = True
					Lines.append(sText[iLineStart:len(sText)])
					print("WrapText() current line is [" + sText[iLineStart:len(sText)] + "]")
					break 
	
	return Lines
	
def CalcTotalLineHeight(Lines, font):
	iTotLineHeight = 0
	for line in Lines:
		if line.isspace() or line == "":
			iTotLineHeight += font.getsize("a")[1] / 2
		else:
			iTotLineHeight += font.getsize(line)[1]
		#print("CalcTotalLineHeight() iTotLineHeight is now " + str(iTotLineHeight))
		
	return iTotLineHeight
		
def FormatText(sText, size, color):
	Lines = []
	base_width = size[0]
	base_height = size[1]
	
	xOffset = .018
	yOffset = .018
	
	offset_width = round(base_width - (base_width * xOffset * 2), 0)
	offset_height = round(base_height - (base_height * yOffset * 2), 0)
	
	iFontSize = 30
	
	print("FormatText() sText length: " + str(len(sText)))
	iTextLen = len(sText)
	if iTextLen <= 140:
		iFontSize = 110
	elif iTextLen <= 260:
		iFontSize = 100
	elif iTextLen <= 380:
		iFontSize = 90
	elif iTextLen <= 500:
		iFontSize = 80
	elif iTextLen <= 620:
		iFontSize = 70
	elif iTextLen <= 740:
		iFontSize = 60
	elif iTextLen <= 860:
		iFontSize = 50
	elif iTextLen <= 980:
		iFontSize = 40
	else:
		iFontSize = 30
		
	print("FormatText() Starting font size is " + str(iFontSize))
	
	font = ImageFont.truetype(PATH + FONT, size = iFontSize, layout_engine = ImageFont.LAYOUT_RAQM)
	
	iTotLineHeight = 0
	
	Lines = WrapText(sText, font, offset_width)
	
	iTotLineHeight = CalcTotalLineHeight(Lines, font)
	
	while iTotLineHeight > offset_height:
		print("FormatText() offset_height exceeded, shrinking font by 5 and trying again")
		iFontSize += (-5)
		
		font = ImageFont.truetype(PATH + FONT, size = iFontSize, layout_engine = ImageFont.LAYOUT_RAQM)
		
		Lines = WrapText(sText, font, offset_width)
		
		iTotLineHeight = CalcTotalLineHeight(Lines, font)
		
	print("FormatText() Final font size is " + str(iFontSize))
	print(Lines)
			
	ImgTxt = Image.new('RGBA', (base_width, base_height), (0,0,0,95))
	draw = ImageDraw.Draw(ImgTxt)
			
	print("FormatText() Base Height = " + str(base_height) + ", Total Line Height = " + str(iTotLineHeight))
	print("FormatText() Vertical offset = " + str(round(((offset_height - iTotLineHeight)/2))))
																		#47.952
																		#1284.048
	y_text = 0
	for x in range(0, len(Lines)):
		width, height = (0, 0)
		if Lines[x].isspace() or Lines[x] == "":
			width, height = font.getsize("a")
			height = height / 2
			#print("FormatText() Empty line found, adding height of " + str(width) + " to vertical offset")
		else:
			width, height = font.getsize(Lines[x])

			draw.text((int(base_width * xOffset), round((offset_height - iTotLineHeight)/2) + y_text), Lines[x], font=font, fill=color)
		y_text += height
		
	# y_text = 0
	# for line in Lines:
		# if line.isspace() or line == "":
			# width, height = font.getsize(".")
		# else:
			# width, height = font.getsize(line)
		# draw.text(((base_width - width) / 2, y_text), line, font=font, fill=color)
		# y_text += height
	
	return ImgTxt

def DrawText(size, sText, color): 
	bck_width = size[0]
	bck_height = size[1]
	
	stest = "d e"
	#print(stest[1].isspace())
	ImgTxt = FormatText(sText, (bck_width - int(bck_width * .075), bck_height - int(bck_height * .075)), color)
	
	ImgFrame = Image.new('RGBA', size, (255,255,255,0))
	
	ImgFrame.paste(ImgTxt, (int((bck_width - ImgTxt.size[0])/2), int((bck_height - ImgTxt.size[1])/2)))

	return ImgFrame
	
def GetBGImg():
	#iNo = randint(1, MAX_IMG_NUM)
	iNo = 9
	
	return Image.open(PATH + "bg_" + str(iNo) + ".png").convert('RGBA')

def CreateImage(sText):
	# create Image object with the input image
	 
	ImgBase = GetBGImg()
	
	color = 'rgb(255, 255, 255)' # black color
	
	ImgTxt = DrawText(ImgBase.size, sText, color)
	 
	# composite the text and base images

	ImgOut = Image.alpha_composite(ImgBase, ImgTxt)
	 
	# save the edited image
	 
	ImgOut.save('test.png', optimize = True, quality = 100)

SampleTweets = ["'You like my outfit?' Dani asked.\n\n'It's stunning, babe,' Quinn said.\n\nHe grabbed the top of her strapless red gown and tugged it down, revealing her swaying girlish jugs. He cupped them with his hands and squeezed them gently. Then he began to suck her nipples.", "'Oh thank God Chastity,' he said to the woman with the dazzling eyes and tightly-bound locks. 'You saved me. How can I ever repay you?'\n\nChastity bent over and pulled down her panties, revealing her luscious tushy.\n\n'You can start by licking my backdoor,' she said.","Calliope knelt in the shallow water and Iain began to lick her dripping dangling petals. Iain eased his impressive stem into her hungry vaginal canal.\n\n'But Iain,' she said, 'People will notice us!!'\n\n'Don't worry baby,' he said, ramming relentlessly into into her.\n\n'That lifeguard is coming towards us!' she said.\n\n'Fuck! I'm gonna cum!' said Iain.\n\n'Wait, not yet!' she cried.\n\n'Too late!' said Iain. 'I'm spurting!' And then, as the lifeguard watched, he grabbed her by the hips and filled her hungry gash with sticky seed.", "'Oh Roberto', she sighed as he held her in his protective arms at the gym, 'I never want this moment to end. I want to stare into your penetrating eyes and put my head against your mighty pectorals forever. I want to dry hump you all night long.'", "'You don't have to hide the truth from me, Chastity,' he said, 'Shane is a successful proctologist and I'm just a lowly stand-up comedian!'\n\n'I don't care about Shane,' she said, 'You're the one I want. And anyway, you have a 9 1/2 inch stalk!'", "Stefan walked in and froze. His wife's Avon Lady lay on the bed totally nude. His wide eyes took in her unbound hair, young figure, heavy thighs, and juicy nether-lips.\n\nThe naked guy next to her was idly kissing her luscious snatch. He looked up at Stefan. 'You want in?' he asked.", "Their masked host ushered them into the banquet hall. In the center of the dining table a beautiful woman lay spread-eagled, completely naked. Her succulent un-sullied flesh was dripping with syrup, her navel was a goblet brimming with liquor, the inside of her thighs were glazed with chocolate, and a single, ripe strawberry was stuffed in her naked hole. 'Gentlemen,' said the prince, 'Let's feast!'\n\n'Lordy!' thought Rafael, 'That's my life drawing model, Ava!'", "Delores slipped out of her dress and pulled down her panties, revealing her shameless muffin. Hunter bent her over the examination table. His beef-rifle was hardening and fully erect. He spread her legs and then eased all 8 inches of his thick girth inside her deep hole and then began to piston into into her. 'But Hunter,' she panted, 'a nurse will hear us!'\n\n'Don't worry, baby,' he said. 'No one will see us in the doctor's office.'\n\nAva watched from her hiding place. Her hands were down her panties and she was frigging her hole furiously.", "'Constance, my dear, I wrote you a poem,' he said.\n\n'What about?' she asked.\n\n'It's about you, my love,' he said. 'It's about your yielding flesh, voluptuous wide womanly hips, shapely legs, puffy cunny, & your gossamer labia.'\n\n'Oh Reginald!' she sighed.", "Chastity slipped out of her dress and pulled down her panties, revealing her vagina. Alistair bent her over the toilet. His meat-missile was hard and fully erect. He spread her legs and then eased all 8 inches of his burning thing inside her dripping chamber and then began to jackhammer into her. 'But Alistair,' she wailed, 'Someone might hear us!!'\n\n'Don't worry, baby,' he said. 'No one will see us in the bathroom at Starbucks.'\n\nRoyce watched from his hiding place. His jeans were unzipped and he was stroking his turgid hard-on feverishly."]
	
	
sTextLong = "Juliette knelt on the boss's desk and Tristan began to lick her hairless outer labia. Despite the the danger of being caught it felt amazing. Tristan eased his hairless penis into her velvet vagina.\n\n'But Tristan,' she said, 'Someone will catch us!!'\n\n'Don't worry baby,' he said, pounding into her.\n\nThe door opened and a tall man walked in. 'Fuck, its my boss!' she said.\n\n'Lord! I'm gonna cum!' said Tristan.\n\n'Wait, not yet!' she cried.\n\n'Too late!' said Tristan. 'I'm ejaculating!'\n\nAnd then, as her boss watched, open-mouthed, he grabbed her by the hips and filled her succulent womb with silken milky man-custard."

sTextMedLong = "Viola entered the bedroom. Connor was wearing nothing but a leather jacket and his limber physique gleamed with oil. Her gazed lingered on his captivating eyes, burly limbs, and bronzed backside.\n\n\"This is a great birthday present, babe,\" she said.\n\n\"This isn't your present,\" said Connor. A tall brunette man stepped thru the bathroom door."

sTextMedShort = "Viola entered the bedroom. Connor was wearing nothing but a leather jacket and his limber physique gleamed with oil. Her gazed lingered on his captivating eyes, burly limbs, and bronzed backside.\n\n\"This is a great birthday present, babe,\" she said."

sTextShort = "\"Please, no!\" Vivienne whimpered, squirming with pleasure as Ruben ravished her lewd bunghole. \"Not while my dentist is watching!\""

KillTestImg()

CreateImage(SampleTweets[randint(0, len(SampleTweets) - 1)])











