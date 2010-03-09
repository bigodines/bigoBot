import twitter 
import time
import os
from datetime import datetime


class BigoBot(object):
	"""
	BigoBot is a Twitter bot for server manipulation. It was designed to download pr0n into our home server. Use at your own risk.
	"""
	
	def __init__(self,username,password):
		self.username = username
		self.api = twitter.Api(username=username, password=password)
		self.tweets = []
		self.latest = None

	def checkTweets(self):
		self.readTweets(self.username)


	def readDirectMessages(self):
		return self.api.GetDirectMessages()

	def readTweets(self,user):
		self.tweets = self.api.GetUserTimeline(user=user, since_id=self.latest)
		self.latest = self.tweets[-1].id

	def check(self):
		self.tweets = self.readDirectMessages()
		for tweet in self.tweets:
			self.download(tweet)
			self.api.DestroyDirectMessage(tweet.GetId())

	def download(self,tweet):
		try:
			url,name = tweet.GetText().split(" ")
			print "downloading:",url,name
			os.system("wget %s; mv *.torrent /discao/HD\ 1TB/torrents/%s" % (url, name))	
		except:
			print "Oops! ", tweet.GetText()
#	def start(self,since_date=None):
#        	pub_time = time.strptime(status.created_at, "%a %b %d %H:%M:%S +0000 %Y")
#        	pub_time = datetime.fromtimestamp(time.mktime(pub_time))


if __name__ == "__main__":
	bb = BigoBot("bigobot","") 
	while True:
		bb.check()
		time.sleep(3600) 
