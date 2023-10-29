import json
from urllib.request import urlopen

url = input("Enter the url: ")
fh = urlopen(url).read()


sum = 0
info = json.loads(fh)
for item in info["comments"]:
    number = item["count"]
    sum += int(number)

print("The sum is: ", sum)