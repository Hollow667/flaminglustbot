#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys, argparse, datetime, threading, traceback

import bodyparts
import locations
import names
import people
import verbs
import misc
import scenes

from io import BytesIO
from random import *
from util import *
from generators import *
from twitter_stuff import *

def ReplyResponder(e, api, iReplyTimer):
	print("Responding to replies every " + str(iReplyTimer) + " seconds...")
	ResponderThread = threading.current_thread()
	
	RespondToReplies(api)
	for x in range(0, iReplyTimer):
		e.wait(1)
		if not ResponderThread.parent_thread.is_alive():
			break
			
	while e.is_set() == False and ResponderThread.parent_thread.is_alive():
		RespondToReplies(api)
		for x in range(0, iReplyTimer):
			e.wait(1)
			if not ResponderThread.parent_thread.is_alive():
				break
	print("Exiting ReplyResponder()")
	
def InitBot(iTweetTimer, iReplyTimer, bTweet = True, iTweets = 1, iGeneratorNo = MAX_GENERATOR_NO):
	print("=*=*=*= FLAMING LUST BOT IS RUNNING (@bot_lust) =*=*=*=\n\n")
	
	sTweet = ""
	bTest = False 
	
	util.TweetHistoryQ = HistoryQWithLog(util.HISTORYQ_FILENAME)
	
	try:
		
		api = InitTweepy()

		e = threading.Event()
		ResponderThread = threading.Thread(target=ReplyResponder, args=(e,api,iReplyTimer))
		ResponderThread.parent_thread = threading.current_thread()
		ResponderThread.start()
		
		if iGeneratorNo == -1:
			iGeneratorNo = MAX_GENERATOR_NO
		else:
			bTest = True
		
		for i in range(0,iTweets):
			#Tweets = [1]
			Gen = None 
			sTweet = ""
			sText = ""
			
			#Tweets = generators.GetChoppedTweets(bTest, iGeneratorNo)
			Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True)
			#print("Generator ID: " + str(Gen.ID))
			while bTweet and not util.TweetHistoryQ.PushToHistoryQ(Gen.ID):
				#print("Generator ID " + str(Gen.ID) + " already in Q")
				Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True)
				#print("New generator ID: " + str(Gen.ID))
			
			sTweet = Gen.GenerateTweet()
			if len(sTweet) > 0:
				if Gen.Type != GeneratorType.Promo:
					sText = GetImgTweetText(Gen)
				
				print("\n===Here is your " + str(len(sTweet)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
				print("[" + sTweet + "]")
				if len(sText) > 0:
					print("Tweet text: [" + sText + "]")
					#print(misc.TweetReplyBuilder().GetReply())
					
				currentDT = datetime.datetime.now()
				if bTweet:
					print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
						
					status = None
						
					if status == None:
						#pass
						#status = UpdateStatus(api, tweet)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet)
						else:
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sText, ImgFile)		
					else:
						#pass
						#status = UpdateStatus(api, tweet, status.id)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet, status.id)
						else:
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sText, ImgFile, status.id)	
					
					#make timer slightly variable +-33%
					if iTweetTimer > 180:
						iRandSecs = iTweetTimer
							
						iRandSecs = randint(int(iRandSecs - (iRandSecs * (1/3))), int(iRandSecs + (iRandSecs * (1/3))))
						print("* Next tweet in " + str(iRandSecs) + " seconds (" + (currentDT + datetime.timedelta(seconds=iRandSecs)).strftime("%H:%M:%S") + ")...")
						time.sleep(iRandSecs)
					else:
						print("* Next tweet in " + str(iTweetTimer) + " seconds (" + (currentDT + datetime.timedelta(seconds=iTweetTimer)).strftime("%H:%M:%S") + ")...")
						time.sleep(iTweetTimer)
	except KeyboardInterrupt:
		print("Ending program ...")
		
		e.set()
		
		sys.exit(1)	
	finally:
		util.TweetHistoryQ.LogHistoryQ()
		print("***Goodbye***")
		
	e.set()
	
def SetGetArgs():
	Parser = argparse.ArgumentParser(prog='lust_bot',description='Run Flaming Lust Bot for Twitter.')
	Parser.add_argument('-tweet', action='store_true', help='send generated tweets to Twitter? (default is False)')
	Parser.add_argument('-numtweets', type=int, default=1, help='number of tweets to generate before quitting (default is 1)')
	Parser.add_argument('-test', type=int, default=-1, help='type of tweet to generate for testing purposes')
	Parser.add_argument('-tweettimer', type=int, default=1800, help='num of seconds to wait before next tweet')
	Parser.add_argument('-replytimer', type=int, default=90, help='num of seconds to wait before running reply routine')
	
	return Parser.parse_args()
			
Args = SetGetArgs()	
print(Args)

InitBot(Args.tweettimer, Args.replytimer, bTweet = Args.tweet, iTweets = Args.numtweets, iGeneratorNo = Args.test)

