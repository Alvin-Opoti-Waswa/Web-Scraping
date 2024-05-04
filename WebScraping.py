#Step 1: Importing Python Libraries and Modules
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#Step 2: Requesting website URL
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)

#Step 3:Extracting Data from selected website
headings = soup.body.findAll('dt')
headings_names = re.findall('id="random.\w+', str(headings))

#Eliminate the first 4 elements
headings_names = [item[4:] for item in headings_names]

#The description of the headings
description = soup.body.findAll('dd')
#Filter the description
headings_description = []

for item in description:
  item = item.text
  item = item.replace('\n', ' ')
  headings_description.append(item)

print(headings_names)
print(headings_description)
#Check if length is equal
print(len(headings_names))
print(len(headings_description))

#Step 4: Creating a data frame
data_frame = pd.DataFrame({'headings_names': headings_names,'headings_description': headings_description})
data_frame
