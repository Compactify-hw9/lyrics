from bs4 import BeautifulSoup
import requests
import re

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
Magnitudes = []
magnitudes = table.select("td:nth-child(3)")
for magnitude in magnitudes:
    Magnitudes.append(magnitude.text)
print(Magnitudes)

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



Longitudes = []
Latitudes = []
for i in longlist:
    html_text = requests.get(i)
    soup = BeautifulSoup(html_text.text)
    table = soup.select('table')
    table = str(table)
    x=table.find('headers="lat"')
    Longitude = table[x+10:x+19]
    number = re.findall("\d+\.\d+", Longitude)
    if number == '':
        Latitude = re.findall("[0-9]+",Latitude)
        print(Latitude)
    else:
        Latitude = number
    Longitudes.append(Longitude)

    x=table.find('headers="lon"')
    Latitude = table[x+10:x+19]
    number = re.findall("\d+\.\d+", Latitude)
    if number == []:
        Latitude = re.findall("[0-9]+",Latitude)
    else:
        Latitude = number

    Latitudes.append(Latitude)
# print(Longitudes[0])
# print(Latitudes[0])
# print(locationsList[0])
# print(dateslist[0])