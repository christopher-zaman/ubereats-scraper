import urllib.request
url = ""
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, "lxml")
#Ubereats web scrapper below

#get titles 
print(soup.prettify())
print("\nFind and print all a tags:\n")
for tag in soup.find_all("span"):
    print("{0}: {1}".format(tag.name, tag.text))
    print(" ")

#get descriptions 
for tag in soup.find_all('span', class_=['menuItem-displayPrice']):
    print(tag.text)
    print(" ")

#print all nav elements for items
for tag in soup.find_all('nav', class_=['ar','as','aj','fn','fo']):
	print("{0}: {1}".format(tag.name,tag.text))
