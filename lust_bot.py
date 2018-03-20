#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import argparse, datetime, tweepy
import twitterauth
import urllib.parse
import twitter

import bodyparts
import locations
import names
import people
import verbs
import misc
import scenes

from random import *
from util import *
from generators import *

TWIT_USERNAME = 'bot_lust'
MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 40
Q_SIZE = 4
REPLIES_FILE_NAME = 'reply_ids.txt'

HistoryQ = []
	
def IsTweetTooLong(sTweet):
	bTooLong = True
	
	if len(sTweet) <= MAX_TWITTER_CHARS:
		bTooLong = False 
	
	return bTooLong

def GenerateTweet(bTest, iGeneratorNo = MAX_GENERATOR_NO):
	Tweet = [0,""]
	sTweet = ""
	iSwitch = 999
	
	iRandMin = 1
	iRandMax = iGeneratorNo
	
	if bTest:
		iRandMin = iGeneratorNo

	Event = misc.Events()
	Exclamation = misc.Exclamations()
	WealthyMan = people.JobWealthyMale()
	WealthyWoman = people.JobWealthyFemale()
	WhiteCollar = people.JobWhiteCollar()
	BlueCollar = people.JobBlueCollar()
	VerbThrust = verbs.VerbThrust()
	VerbMakeLove = verbs.VerbMakeLove()
	VerbEjaculate = verbs.VerbEjaculate()
	VerbForeplay = verbs.VerbForeplay()
	MaleName = names.NamesMale()
	FemaleName = names.NamesFemale()
	MaleFWB = people.MaleFWB()
	FemaleFWB = people.FemaleFWB()
	FemBodyParts = bodyparts.BodyFemale()
	MaleBodyParts = bodyparts.BodyMale()
	Mouth = bodyparts.Mouth()
	Breasts = bodyparts.Breasts()
	Thighs = bodyparts.Thighs()
	Vagina = bodyparts.Vagina()
	Ass = bodyparts.AssFemale()
	Penis = bodyparts.Penis()
	Semen = bodyparts.Semen()
	
	iSwitch = randint(iRandMin, iRandMax)
	while not bTest and iSwitch in HistoryQ:
		iSwitch = randint(iRandMin, iRandMax)
	
	HistoryQ.insert(0, iSwitch)
	if len(HistoryQ) > Q_SIZE:
		HistoryQ.pop()
	
	if iSwitch == 1:
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
	#elif iSwitch == ??:
		#He opened the door and his heart skipped a beat. Angela was lying on the bed naked. [Describe] She opened her naked legs, reached down and spread her gleaming pussy lips. "Happy birtday, baby," she said.
	#elif iSwitch == ??:
		#I've got a present for you, she said. What's that? he asked her. She [bent over and pulled her panties aside, revealing her little starfish.] [lifted up her short skirt revealing that she wasn't wearing any panties. He could clearly see her smooth pussy lips and her inner folds.] [pulled her titties out of her blouse. They were large and gleaming with oil.]
	#elif iSwitch == ??:
		#I still love you, Veronica, he said, even after all these years. I love you too, Steve, said Veronica. I've loved you since the first time you titty fucked me in the men's bathroom
	#elif iSwitch == ??:
		#Raoul entered, wearing a white robe. He whipped the towel off Rosanna, exposing her naked form. He began to gently massage her {body parts}. Rosanna opened her eyes. His robe was now open, exposing his massive swollen
	#elif iSwitch == ??:
		#'Oh baby,' she said. 'I love you so much. I just want to be with you and make you happy. Tell me what I can do,' she said, giving him a peck on the lips.
		#'I want {to fuck your big titties / to put my finger in your butthole / to put my balls in your mouth / you to eat out my starfish },' he said.
	#elif iSwitch == ??:
		#'I own you now,' he said to the babysitter. "I own your your pretty mouth, I own your lickable tits, I own the dripping folds of your cunt and I even own..." He leaned forward, and whispered in her ear, "Your tight little starfish."
		#"Ooh, yes general," she said.
	#elif iSwitch == ??:
		#'It was just a silly bet,' he said.\n\n
		#'No, fair is fair,' she said, pulling down her panties. 'I said that you could use my cocksock any way you want, right here in the woods, and I never go back on a bet.'  
	#elif iSwitch == ??:
		#'Kylie! Hi!' he said to the barista. 'You two know each other?' Sam's girlfriend asked. 'Oh yes,' said Kylie. 'Sam sucked my titties back in college.'
	else:
		print("iSwitch not found: " + str(iSwitch))
		
	Tweet[0] = iSwitch
	Tweet[1] = sTweet
	return Tweet
	
def ChopTweet(sTweet):
	Tweets = []
	iLen = len(sTweet)
	iTargetLen = MAX_TWITTER_CHARS - 4
	iTweetNo = 1

	while len(sTweet) > iTargetLen:
		iLastChar = iTargetLen
		
		while not sTweet[iLastChar].isspace():
			iLastChar = iLastChar - 1
			
		Tweets.append(str(iTweetNo) + ") " + sTweet[0:iLastChar])
		iTweetNo = iTweetNo + 1
		sTweet = sTweet[iLastChar + 1:]
	Tweets.append(str(iTweetNo) + ") " + sTweet)
	
	return Tweets
	
def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets) > 1:
			if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
				Tweets[len(Tweets) - 1] += sHashtag
		else:
			if len(Tweets[0]) + len(sHashtag) < MAX_TWITTER_CHARS:
				Tweets[0] += sHashtag

	return Tweets
	
	
def RespondToReplies(api):
	my_screen_name = 'bot_lust'
	my_userid = '973202601545273344'
	max_id = None
	max_tweets = 60
	
	HistoricReplies = []
	with open(REPLIES_FILE_NAME) as ReadReplyFile:
		HistoricReplies = ReadReplyFile.read().splitlines()
		
	#print("Historic reply IDs:")
	#print(HistoricReplies)
		
	query = "to:" + my_screen_name
		
	try:		
		replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

		for reply in replies:
			if not reply.user.id_str == my_userid:
				if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
	 
					#print(reply.id_str)
					#print(reply.text)
					#print(reply.user.screen_name)
					
					api.update_status("@" + reply.user.screen_name + " " + misc.TweetReplyBuilder().GetReply(), in_reply_to_status_id = reply.id_str)
					
					with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
						WriteReplyFile.write(str(reply.id_str) + "\n")
		
	except tweepy.TweepError as e:
		print("***ERROR*** [" + e.reason + "]")
	
def InitBot(iSleepTimer, bTweet = True, iTweets = 1, iGeneratorNo = MAX_GENERATOR_NO):
	print("=*=*=*= FLAMING LUST BOT IS RUNNING (@bot_lust) =*=*=*=\n\n")
	
	sTweet = ""
	bTest = False 
	
	CONSUMER_KEY = twitterauth.ConsumerKey
	CONSUMER_SECRET = twitterauth.ConsumerSecret
	ACCESS_KEY = twitterauth.AccessKey
	ACCESS_SECRET = twitterauth.AccessSecret
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	
	api = tweepy.API(auth)
	
	if iGeneratorNo == 0:
		iGeneratorNo = MAX_GENERATOR_NO
	else:
		bTest = True
	
	for i in range(0,iTweets):
		Tweet = [0,""]
		Tweet = GenerateTweet(bTest, iGeneratorNo)
		print("===Here is your " + str(len(Tweet[1])) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
		Tweets = [1]
		if IsTweetTooLong(Tweet[1]):
			Tweets = ChopTweet(Tweet[1])
			Tweets = AddHashtag(Tweets)
			for tweet in Tweets:
				print("[" + tweet + "](" + str(len(tweet)) + " chars)")
		else:
			Tweets[0] = Tweet[1]
			Tweets = AddHashtag(Tweets)
			print("[" + Tweets[0] + "](" + str(len(Tweets[0])) + " chars)")
		
		#print(misc.TweetReplyBuilder().GetReply())
		
		currentDT = datetime.datetime.now()
		if bTweet:
			print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
				
			status = None
			
			RespondToReplies(api)
				
			try:
				for tweet in Tweets:
					if status == None:
						#pass
						status = api.update_status(tweet)
							
					else:
						#pass
						status = api.update_status(tweet, in_reply_to_status_id = status.id)
			except tweepy.TweepError as e:
				print("***ERROR*** [" + e.reason + "]")				
				
			#make timer slightly variable +-33%
			if iSleepTimer > 180:
				iRandSecs = iSleepTimer
					
				iRandSecs = randint(int(iRandSecs - (iRandSecs * (1/3))), int(iRandSecs + (iRandSecs * (1/3))))
				print("* Next tweet in " + str(iRandSecs) + " seconds (" + (currentDT + datetime.timedelta(seconds=iRandSecs)).strftime("%H:%M:%S") + ")...")
				time.sleep(iRandSecs)
			else:
				print("* Next tweet in " + str(iSleepTimer) + " seconds (" + (currentDT + datetime.timedelta(seconds=iRandSecs)).strftime("%H:%M:%S") + ")...")
				time.sleep(iSleepTimer)
		
	print("* Done!")
	
def SetGetArgs():
	Parser = argparse.ArgumentParser(prog='lust_bot',description='Run Flaming Lust Bot for Twitter.')
	Parser.add_argument('-tweet', action='store_true', help='send generated tweets to Twitter? (default is False)')
	Parser.add_argument('-numtweets', type=int, default=1, help='number of tweets to generate before quitting (default is 1)')
	Parser.add_argument('-test', type=int, default=0, help='type of tweet to generate for testing purposes')
	Parser.add_argument('-sleeptimer', type=int, default=1200, help='num of seconds to wait before next tweet')
	
	return Parser.parse_args()
			
Args = SetGetArgs()	
print(Args)

InitBot(Args.sleeptimer, bTweet = Args.tweet, iTweets = Args.numtweets, iGeneratorNo = Args.test)

