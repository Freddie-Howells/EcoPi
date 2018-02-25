#! /usr/bin/env python
import tweepy
from datetime import datetime

API_KEY = 'LnMq4WNWZQsBdPdzHouYhoSOE'
API_SECRET = 'SrivtlUGF9ylpQLSLcSKiBO9hz8Tbq4QumV4xjtzuc2jcjPxIN'
ACCESS_TOKEN = '965591104845504512-mCjsacEFhS5kVeVlUziApzUSLeTiayv'
ACCESS_TOKEN_SECRET = 'RDWji3NombIIw2a8IBd9se5dWuGkGZOV4PTgN0vzOus5d'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tempfile = open("/sys/bus/w1/devices/28-0417c1b18eff/w1_slave")
thetext = tempfile.read()
tempfile.close()
tempdata = thetext.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = str(temperature / 1000)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')

if temperature>='22':
	api.update_status(temperature + " C at " + thetime + ". Do you want to turn the heating off?") 

if temperature<='17':
	api.update_status(temperature + " C at " + thetime + ". Do you want to turn the heating on?") 


print(temperature)
