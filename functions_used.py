import requests
from bs4 import BeautifulSoup

def patient():
    URL = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_ = 'content-inner')
    count = {"data":[]}
    primary = {}
    numbers = results.find_all('div', id = 'maincounter-wrap')
    for number in numbers:
        text = number.find('h1')
        units = number.find('span')
        primary[text.text] = units.text
    count["data"].append(primary)
    return count

def weather_report():
    page = requests.get("https://weather.com/en-IN/weather/tenday/l/e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668")

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
    table = soup.find_all("table",{"class":"twc-table"})

    weather={"data": []}
    for items in table:
        for i in range(len(items.find_all("tr"))-1):
            d = {}  
            d["Day"]=items.find_all("span",{"class":"day-detail"})[i].text
            d["Temperature"]=items.find_all("td",{"class":"temp"})[i].text[:2]
            d["Windspeed"]=items.find_all("td",{"class":"wind"})[i].text  
            d["Event"]=items.find_all("td",{"class":"description"})[i].text 
            weather['data'].append(d)
            
    return weather