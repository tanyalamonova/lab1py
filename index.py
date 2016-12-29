import requests
import re

def ShowCheckedPages(urls):
		global mainUrl
		print()
		print("We've checked the following pages:")
		for url in urls:
			if(not url.startswith('http://')):
				url = mainUrl + url
			print(url)
		print()

def ShowwAllEmails(emails):
		print()
		print("We've got the following emails:")
		for email in emails:
			print(email)

def AddEmails(emails):
		global allMails
		for email in emails:
			if email not in allMails:
				allMails.append(email)

def ParsePage(url):
	global count
	global mainUrl
	print("Current page:", url)
	if count < 1:
		checkedPages.append(url)
	websiteText = requests.get(url)
	urls = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', websiteText.text)))
	for currenturl in urls:
		if not currenturl.startswith('/') or not currenturl.endswith('/'):
			urls.remove(currenturl)
	reobj = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
	emails = list(set(re.findall(reobj, websiteText.text)))
	AddEmails(emails)
	for currenturl in urls:
		if count <= 20:
			count += 1
			if not currenturl.startswith('http://') and currenturl not in checkedPages:
				checkedPages.append(currenturl)
				ParsePage(mainUrl + currenturl)

allMails = []
checkedPages = []
count = 0
mainUrl = "http://mosigra.ru"
ParsePage(mainUrl)
ShowCheckedPages(checkedPages)
ShowwAllEmails(allMails)
