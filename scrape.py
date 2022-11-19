from bs4 import BeautifulSoup
import requests

year = 2022
originalURL = 'https://earthquakescanada.nrcan.gc.ca/recent/2022/index-en.php#wb-auto-5'
newURL = originalURL[0:45] + str(year) + originalURL[-23:]

html_text = requests.get('https://earthquakescanada.nrcan.gc.ca/recent/2022/index-en.php#wb-auto-5').text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('tbody')

locations = table.find_all('a')
locationsList = []
for location in locations:
    if location.text != "report":
        locationsList.append(location.text)

dates = table.find_all('span')
datesList = []
for date in dates:
    if date.text != "Felt" and date.text != "Not felt":
        datesList.append(date.text)

print(locationsList)
print(datesList)