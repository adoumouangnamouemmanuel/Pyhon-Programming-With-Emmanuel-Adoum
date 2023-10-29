from urllib.request import urlopen
import xml.etree.ElementTree as ET

#input url and parsing file

url = input("Enter the url: ")
fh = urlopen(url).read()

fh_parsing = ET.fromstring(fh)
counts = fh_parsing.findall(".//count")

sum = 0
for count in counts:
    number = count.text
    sum += int(number)

print("The sum is: ", sum)