#step 1: import libraries
#typically you'd add a requirements.txt file to your project and then import the libraries you need by running "pip install -r requirements.txt"
#but I haven't done that here since part of the tutorial is learning and practicing how to install libraries using pip

import pandas as pd
import tabulate as tabulate

#step 2: find the url of a page that has tables that you would like to extract
url = "https://www.programiz.com/python-programming/keyword-list"

#step 3: use the read_html method in pandas and give it the url of the page you want to scrape for HTML tables
data = pd.read_html(url)

#the data is captured at this point, but if you want to print it to the screen, follow the steps below

#step 4 (optional): prettify the result for easier reading
pretty = tabulate.tabulate(data[0], headers='keys', tablefmt='psql')

#step 5 (optional): print the results, or just use the data as you like
print(pretty)