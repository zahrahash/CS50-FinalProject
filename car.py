import requests
from bs4 import BeautifulSoup
import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'car')

cursor = cnx.cursor()
name = []
year = []
price = []
mile = []
new_name = []
new_year = []
new_price = []
new_mile = []

url = ['https://www.truecar.com/used-cars-for-sale/listings/bmw/', 
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=2',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=3',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=4',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=5',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=6',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=7',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=8',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=9',
'https://www.truecar.com/used-cars-for-sale/listings/bmw/?page=10'
]

for i in url:
    URL_page = requests.get(i)
    soup = BeautifulSoup(URL_page.text, 'html.parser')

    name = soup.find_all('span', attrs={"class":"vehicle-header-make-model text-truncate"})
    price = soup.find_all('div', attrs= {"data-test":"vehicleListingPriceAmount"})
    mile = soup.find_all('div', attrs={"data-test":"vehicleMileage"})

    for i in price:
        price = i.text
        price = price[1:len(price)]
        price = price.split(',')
        price = int(price[0] + price[1])
        new_price.append(price)
            
    for j in mile:
        mile = j.text
        mile = mile[0:-6] 
        mile = mile.split(',')
        mile = int(mile[0] + mile[1])
        new_mile.append(mile)

    for k in name:
        name = k.text
        new_name.append(name)


    for x, y, k in zip(new_name, new_price, new_mile) :
        cursor.execute('insert into moshakhasat value(\'%s\', \'%s\', \'%s\')' % (x ,y ,k))

cnx.commit()
cnx.close()