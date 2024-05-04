#Step 1
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#Step 2
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)

#Step 3
headings = soup.body.findAll('dt')
headings_names = re.findall('id="random.\w+', str(headings))

print(headings_names)
