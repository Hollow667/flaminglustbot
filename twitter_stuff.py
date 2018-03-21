# Twitter-related functions (Tweepy-based)

import misc
import tweepy
import twitterauth

REPLIES_FILE_NAME = 'reply_ids.txt'

def InitTweepy():
	api = None
	
	CONSUMER_KEY = twitterauth.ConsumerKey
	CONSUMER_SECRET = twitterauth.ConsumerSecret
	ACCESS_KEY = twitterauth.AccessKey
	ACCESS_SECRET = twitterauth.AccessSecret
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	
	api = tweepy.API(auth)
	
	return api
	
def UpdateStatus(api, Tweet, in_reply_to_status_id = ""):
	try:
		status = api.update_status(Tweet, in_reply_to_status_id)
	except tweepy.TweepError as e:
		print("***ERROR*** [" + e.reason + "]")	
		
	return status 
	

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