# flaminglustbot

This is a twitter bot designed to tweet out steamy 'love scenes' generated from word lists. It will also reply to anyone who replies to it with a tweet plugging one of its non-existant, auto-generated erotic ebooks. This bot was coded in python. It uses the **tweepy** library to access Twitter's API. It uses the **pillow** library to create images.

***WARNING***
This bot generates explicit adult content! You must be 18+ to use or modify this bot!

## features
* Bot talks back: replies to users that reply to its tweets
* Creates and tweets images: images are in memory only and not stored on drive
* Multi-threaded: replies are handled separately from regular tweets

## running the bot

The bot uses the python library **tweepy** to access the twitter API. It requires a file called twitterauth.py which is **not** contained in this repo. you must create your own file and include your own twitter authentication codes, obtained from https://apps.twitter.com/.

To run this bot:
```
lust_bot [-tweet] [-numtweets NUMTWEETS] [-test TEST] [-tweettimer TWEETTIMER] [-replytimer REPLYTIMER]
```
All args optional, but you must include **-tweet** if you want the bot to actually tweet what it generates.

## me

This is my first python program. I am more experienced with strict object-oriented languages like Java and C#. Please excuse the non-pythonic quirks of my code.

## feel free to fork and steal

I spent way too much time working on this silly bot. Some of the features I've implemented pretty poorly documented. Hopefully the code can be useful to other python devs. If you are forking or stealing large chunks of code wholesale, please be kind and give me credit and include a link to this repo.
