# scrape_gas_prices_script.py

import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
from pymongo import MongoClient

def scrape_gas_prices():
    url = "https://www.essencemontreal.com/prices.php?l=f&prov=QC&city=Montreal"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = soup.find_all('td', {'class': ['greencell', 'redcell', 'pricecell']})
    stations = soup.find_all('td', {'class': 'stationcell'})
    cities = soup.find_all('td', {'class': 'citycell'})
    times_users = soup.find_all('td', {'class': 'usercell'})

    gas_prices = []

    for price, station, city, time_user in zip(prices, stations, cities, times_users):
        gas_station = " ".join(station.stripped_strings)
        gas_city = " ".join(city.stripped_strings)
        gas_price = " ".join(price.stripped_strings)
        gas_time_user = " ".join(time_user.stripped_strings)

        # Splitting gas_time_user into time and user
        gas_time, *gas_user = gas_time_user.split(maxsplit=1)
        gas_user = ' '.join(gas_user)

        # Get today's date
        today = date.today()

        # Add today's date to the gas price information
        gas_prices.append((gas_price, gas_station, gas_city, gas_time, gas_user, str(today)))

    # Convert the list of tuples to a pandas DataFrame
    df = pd.DataFrame(gas_prices, columns=['price', 'station', 'city', 'time', 'user', 'date'])

    # Save data to MongoDB
    client = MongoClient("mongodb+srv://trivinochris124:Ihavethepower1!@cluster0.yl5qyo0.mongodb.net/sample_mflix?retryWrites=true&w=majority")
    db = client.gas_prices_db
    collection = db['gas_prices']
    records = df.to_dict(orient='records')
    collection.insert_many(records)
    
    
