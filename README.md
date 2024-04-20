# WEB SCRAPING
I am creating a database by extracting html elements from a webpage.
## The Modules Used:
Urllib.request -> The urllib.request module, which is a part of Python's standard library. Is used to make HTTP requests to web pages.

BeautifulSoup -> We import the BeautifulSoup class from the bs4 (Beautiful Soup 4) library. This class is the main tool we'll use for parsing HTML.

Regex -> We import Python's built-in re module, which stands for Regular Expressions. Regular expressions are a powerful tool for searching and manipulating strings.

Pandas -> Lastly we import the pandas library and assigns it the alias pd. pandas is a powerful data manipulation and analysis library in Python.

#### In Summary:
We use these import statements set up the basic tools we'll need for web scraping: fetching web pages (urllib.request), parsing HTML (BeautifulSoup), handling regular expressions (re), and data manipulation (pandas).

## Step By Step Walk-Through:

#### Step 1: 
Setup the import statements to import the python libraries and modules stated above.

#### Step 2:
Choose the HTML website you wish to scrape data from and place the it's url in x {page = urllib.request.urlopen("x")}

Here, we're using the urllib.request module to fetch the contents of a web page.This line sends a request to the web server hosting that page and retrieves the HTML content of the page.Once you've fetched the page, its content will be stored in the variable named (page).

Next, we pass the HTML content stored in the page variable to the BeautifulSoup constructor.(soup=bs(page)).

In summary these two lines of code fetch a web page's HTML content and then use BeautifulSoup to parse and create a structured representation of that content, making it easier for us to work with and extract the information we need.

#### Step 3:
