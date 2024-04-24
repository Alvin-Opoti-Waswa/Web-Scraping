import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen('https://peps.python.org/pep-0008/')
soup = bs(page)


headings = soup.body.findAll('a')
headings_names = re.findall('href="([^"]+)"', str(headings))

print(headings_names)
