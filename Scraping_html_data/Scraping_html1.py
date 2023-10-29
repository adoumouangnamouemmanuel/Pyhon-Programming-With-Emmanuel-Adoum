import urllib.request, re
from bs4 import BeautifulSoup


try:
    #input url and request
    url = input("Enter the url: ")
 
    fh = urllib.request.urlopen(url).read()

    #parsing the file
    soup = BeautifulSoup(fh, 'html.parser')

    sum = 0
    comments = soup.find_all("span", class_='comments')
    for comment in comments:
        numbers = re.findall("([0-9]+)", comment.decode())
        for number in numbers:
            sum += int(number)

    print(sum)

except:
    print("Privide the correct link!")