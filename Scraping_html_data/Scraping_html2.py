from urllib.request import urlopen
from bs4 import BeautifulSoup

#Request
url = input("Enter the url: ") #link in the readme / 2
fh = urlopen(url).read()

#Parsing html file
soup = BeautifulSoup(fh, "html.parser")

#retrieving all the a tags
tags = soup("a")
lst = list()
for tag in tags:
    link = tag.get("href", None)
    lst.append(link)

#Repeating the process 7 times with the link at position 18
i = 0
while i < 5:
    url = lst[17]
    fh = urlopen(url).read()
    soup = BeautifulSoup(fh, "html.parser")
    tags = soup("a")
    lst = list()
    for tag in tags:
        link = tag.get("href", None)
        lst.append(link)
    i += 1

#Recuperate the text between the a tag at the 7th round
url = lst[17]
fh = urlopen(url).read()
soup = BeautifulSoup(fh, "html.parser")
tags = soup("a")
print("The correct name is: ", tags[17].text)
