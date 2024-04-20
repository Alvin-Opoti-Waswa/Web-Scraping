import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen('https://wseiz.pl/uczelnia/wydzial-inzynierii-i-zarzadzania/informatyka-i-stopnia/')
soup = bs(page)
