from keyboard import send, wait, write
from mouse import get_position as update_mouse_pos
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
print("quotes generated \nplease press F6 on your keyboard once in edge, and signed into your Cranbury School google account")
mousepos = (100,100)
wait('f6')
send('ctrl+t')
write("https://docs.google.com/forms/d/e/1FAIpQLSdGxOdKkyleSepQElzmWf3DEpfK2CwcHMz5RZ5a_hO88XaWJw/viewform?usp=sf_link")
send('enter')
for i in range(len(quoteslist)):

	time.sleep(1.5)
	for a in range(3): send('tab')
	send('down+tab')
	write(quoteslist[i])
	send('tab+enter')
	time.sleep(2)
	for b in range(4): send('tab')
	send('enter')
	time.sleep(0.5)
	send('tab')
	time.sleep(0.5)
	send('enter')
	time.sleep(0.5)
	mousepos = update_mouse_pos()
	if mousepos == (0,0):
		break
log.write(f"{time.asctime(time.localtime())}: Execution Completed. Will exit")
print("Execution completed.")