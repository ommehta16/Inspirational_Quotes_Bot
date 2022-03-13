import pyautogui
from assets.list_interperet import listmaker
import os.path
import sys
import time
settings = open("settings.covid", "r", encoding='utf8')
settingslist = settings.readlines()
file = os.path.abspath(settingslist[0]) #Later, could be cool to have a file picker w/ tk
log = open("log.bait", "a")

#Kill the program if it's not being pointed to right file
if not os.path.exists(file):
	log.write(f'{time.asctime(time.localtime())}: File "{file}" does not exist \n')#maybe make specific funcs for log errors
	sys.exit(0)

quotesfile = open(file, encoding='utf8')
quotes = quotesfile.read()
quotes = listmaker.fixdash(quotes)
quotesworkingfile = open("quoteswork", "w")
quotesworkingfile.write(quotes)
quotesworkingfile.close()
quotesworkingfile = open("quoteswork", "r")
quoteslist = quotesworkingfile.readlines()
quoteslist = listmaker.validify_quotes(quoteslist)
for i in range(len(quoteslist)):
	print(quoteslist[i])
print(len(quoteslist))