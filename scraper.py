import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas

url = "https://www.slickcharts.com/sp500"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

answer = requests.get(url, headers=headers)
soup = bs(answer.text, features="html.parser")

# Find all <tr> elements
rows = soup.find_all("tr")

# Initialize an empty list to store symbols
symbols = []

# Iterate through each row
for row in rows:
    # Get all <td> elements in the row
    cells = row.find_all("td")
    
    # Check if the row has at least 3 <td> elements
    if len(cells) > 2:
        # Find the <a> tag inside the 3rd <td>
        a_tag = cells[2].find("a")
        if a_tag:  # Check if the <a> tag exists
            symbols.append(a_tag.text.strip())  # Add the text to the list

# Print the extracted symbols

df = pandas.DataFrame(sorted(symbols), columns=["Ticker"])
df.to_csv("sp500.csv", index=False)


