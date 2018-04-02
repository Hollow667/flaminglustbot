# Twitter-related functions (Tweepy-based)

from io import BytesIO
from generators import *
import misc
import tweepy
import twitterauth

from random import *
from util import *

REPLIES_FILE_NAME = "reply_ids.txt"
HASHTAG_LOVESCENE = "#lovescene"
HASHTAG_BOOKTITLE = "#book"

def InitTweepy():
	api = None
	
	# These twitter access codes are stored in a seperate file not included in the github repo. You must create your own. simply name it twitterauth.py and include the four variables below: ConsumerKey, ConsumerSecret, AccessKey, AccessSecret. you get these codes from https://apps.twitter.com/
	CONSUMER_KEY = twitterauth.ConsumerKey
	CONSUMER_SECRET = twitterauth.ConsumerSecret
	ACCESS_KEY = twitterauth.AccessKey
	ACCESS_SECRET = twitterauth.AccessSecret
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	
	api = tweepy.API(auth, wait_on_rate_limit = True)
	
	return api
	
def UpdateStatus(api, Tweet, in_reply_to_status_id = ""):
	status = None 
	bTryToTweet = True 
	
	while bTryToTweet:
		try:
			status = api.update_status(Tweet, in_reply_to_status_id)
			bTryToTweet = False 
		except tweepy.TweepError as e:
			print("***TWITTER ERROR*** " + e.reason)	
			# if twitter throws certain over capacity errors, wait a few seconds and try again
			print(e.api_code)
			code = e.api_code
			if code in [88, 130, 131]:
				bTryToTweet = True
				time.sleep(30)
			else:
				bTryToTweet = False

	return status 

def UpdateStatusWithImage(api, Tweet, ImgFile, in_reply_to_status_id = ""):
	status = None 
	bTryToTweet = True 
	
	while bTryToTweet:
		try:
			status = api.update_with_media("tweet.png", Tweet, in_reply_to_status_id, file = ImgFile)
			bTryToTweet = False 
		except tweepy.TweepError as e:
			print("***TWITTER ERROR*** " + e.reason)	
			# if twitter throws certain over capacity errors, wait a few seconds and try again
			print(e.api_code)
			code = e.api_code
			if code in [88, 130, 131]:
				bTryToTweet = True
				time.sleep(30)
			else:
				bTryToTweet = False

	return status 

def RespondToReplies(api):
	my_userid = '973202601545273344'
	max_id = None
	max_tweets = 60
	
	HistoricReplies = []
	with open(REPLIES_FILE_NAME) as ReadReplyFile:
		HistoricReplies = ReadReplyFile.read().splitlines()
		
	#print("Historic reply IDs:")
	#print(HistoricReplies)
		
	query = "to:" + TWIT_USERNAME
		
	try:		
		replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

		for reply in replies:
			if not reply.user.id_str == my_userid:
				if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
					print("Reply found: " + reply.text)
					iFlag = 0
					if HASHTAG_BOOKTITLE in reply.text.lower():
						iFlag = 1
					elif HASHTAG_LOVESCENE in reply.text.lower():
						iFlag = 2
					else:
						iCoinFlip = randint(1,2)
						if iCoinFlip == 2:
							iFlag  = 2
						else:
							iFlag = 1
					
					if iFlag == 1: 
						api.update_status("@" + reply.user.screen_name + " " + misc.TweetReplyBuilder().GetReply(), in_reply_to_status_id = reply.id_str)	
					elif iFlag == 2:
						Tweets = [1]
			
						sPrefix = "@" + reply.user.screen_name + " "
						#Tweets = generators.GetChoppedTweets(False, MAX_GENERATOR_NO, sPrefix, bAllowPromo = False)
						Gen = GetTweet(False, bAllowPromo = False)
						sTweet = Gen.GenerateTweet()

						status = None
						print("===Here is your " + str(len(sTweet)) + " char tweet===")
						#for tweet in Tweets:
						print("[" + sTweet + "]")
						
						if status == None:	
							# status = UpdateStatus(api, tweet, reply.id_str)
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sPrefix, ImgFile, reply.id_str)	
						else:
							# status = UpdateStatus(api, tweet, status.id)
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sPrefix, ImgFile)	
					
					with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
						WriteReplyFile.write(str(reply.id_str) + "\n")
		
	except tweepy.TweepError as e:
		print("***ERROR*** [" + e.reason + "]")