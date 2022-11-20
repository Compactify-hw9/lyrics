from bs4 import BeautifulSoup
import requests, re, csv

for i in range(14):
    year = 2022 - i
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
        soup = BeautifulSoup(html_text.text, 'lxml')
        table = soup.select('table')
        table = str(table)
        x=table.find('headers="lat"')
        Longitude = table[x+14:x+19]
        number = re.findall("\d+\.\d+", Longitude)
        if number == '':
            Longitude = re.findall("[0-9]+",Longitude)
            print(Longitude)
        else:
            Latitude = number
        Longitudes.append(Longitude)

        x=table.find('headers="lon"')
        Latitude = table[x+14:x+19]
        number = re.findall("\d+\.\d+", Latitude)
        if number == '':
            Latitude = re.findall("[0-9]+",Latitude)
        else:
            Latitude = number

        Latitudes.append(Latitude)

    csvName = str(year) + 'earthquake.csv'
    for i in range(len(locationsList)):
        try:
            data_to_append = [
                [locationsList[i], datesList[i], Magnitudes[i], Longitudes[i], float(Latitudes[i][0])]
            ]
        except IndexError:
            continue
        file = open(csvName, 'a', newline='')
        writer = csv.writer(file)
        writer.writerows(data_to_append)
    file.close()
  