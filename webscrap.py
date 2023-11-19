import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "https://streetbazaar.net/listing"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

data=[]

# Extract information
img_url = soup.find('img', class_='rtcl-thumbnail')['src']
category = soup.find('div', class_='category').find('a').text
title = soup.find('h3', class_='listing-title').find('a').text

# Check if the price is available
price_elem = soup.find('div', class_='rtcl-price-type-label')
price = 'On Call' if price_elem else 'Price not available'

data.append([title, category, img_url, price_elem])



# Store the information in a pandas dataframe
df = pd.DataFrame(data, columns=['Title', 'Category', 'Img_url', 'price_elem'])

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)


# Export the data to a CSV file
df.to_json('streetbazaarproductdata.json', orient='records', lines=True)