#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import argparse, datetime

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
from twitter_stuff import *

TWIT_USERNAME = 'bot_lust'
MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
Q_SIZE = 5

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

	iRandMin = 0
	iRandMax = iGeneratorNo
	
	if bTest:
		iRandMin = iGeneratorNo
	
	iSwitch = randint(iRandMin, iRandMax)
	while not bTest and iSwitch in HistoryQ:
		iSwitch = randint(iRandMin, iRandMax)
	
	HistoryQ.insert(0, iSwitch)
	if len(HistoryQ) > Q_SIZE:
		HistoryQ.pop()
	
	if iSwitch == 0:
		sTweet = GeneratorPromo().GenerateTweet()
	elif iSwitch == 1:
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
	elif iSwitch == 41:
		sTweet = Generator32().GenerateTweet()
	elif iSwitch == 42:
		sTweet = Generator33().GenerateTweet()
	elif iSwitch == 43:
		sTweet = Generator34().GenerateTweet()
	elif iSwitch == 44:
		sTweet = Generator35().GenerateTweet()
	#elif iSwitch == ??:
		#He opened the door and his heart skipped a beat. Angela was lying on the bed naked. [Describe] She opened her naked legs, reached down and spread her gleaming pussy lips. 
	#elif iSwitch == ??:
		#I still love you, Veronica, he said, even after all these years. I love you too, Steve, said Veronica. I've loved you since the first time you titty fucked me in the men's bathroom
	#elif iSwitch == ??:
		#Raoul entered, wearing a white robe. He whipped the towel off Rosanna, exposing her naked form. He began to gently massage her {body parts}. Rosanna opened her eyes. His robe was now open, exposing his massive swollen
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
	
def InitBot(iSleepTimer, bTweet = True, iTweets = 1, iGeneratorNo = MAX_GENERATOR_NO):
	print("=*=*=*= FLAMING LUST BOT IS RUNNING (@bot_lust) =*=*=*=\n\n")
	
	sTweet = ""
	bTest = False 
	
	api = InitTweepy()
	
	if iGeneratorNo == -1:
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
				
			for tweet in Tweets:
				if status == None:
					#pass
					#status = api.update_status(tweet)
					status = UpdateStatus(api, tweet)
							
				else:
					#pass
					#status = api.update_status(tweet, in_reply_to_status_id = status.id)
					status = UpdateStatus(api, tweet, status.id)
							
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
	Parser.add_argument('-test', type=int, default=-1, help='type of tweet to generate for testing purposes')
	Parser.add_argument('-sleeptimer', type=int, default=1200, help='num of seconds to wait before next tweet')
	
	return Parser.parse_args()
			
Args = SetGetArgs()	
print(Args)

InitBot(Args.sleeptimer, bTweet = Args.tweet, iTweets = Args.numtweets, iGeneratorNo = Args.test)

