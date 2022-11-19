from bs4 import BeautifulSoup
import requests

year = 2022
originalURL = 'https://earthquakescanada.nrcan.gc.ca/recent/2022/index-en.php#wb-auto-5'
newURL = originalURL[0:45] + str(year) + originalURL[-23:]

html_text = requests.get(newURL).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('tbody')

locations = table.find_all('a')
locationsList = []
longlist = []
for location in locations:
    if location.text != "report":
        locationsList.append(location.text)
        longlist.append(location)
    

dates = table.find_all('span')
datesList = []
for date in dates:
    if date.text != "Felt" and date.text != "Not felt":
        datesList.append(date.text)
for i in range (0,len(longlist)):
    longlist[i]=str(longlist[i])
    longlist[i]=longlist[i][9:]
    longlist[i]=('https://earthquakescanada.nrcan.gc.ca') + longlist[i]
    longlist[i].replace(str(locationsList[i]),'')
    longlist[i]=longlist[i][:76]

print(longlist)

for i in range (0,len(longlist)):
    html_text = requests.get(longlist[i]).text
    soup = BeautifulSoup(html_text, 'lxml')